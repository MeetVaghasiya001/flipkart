from parser import featch_urls
from db import connection, insert_product_urls, update_status
from concurrent.futures import ThreadPoolExecutor, as_completed




def process_url(url):
    result = featch_urls(url)

    page_url = []
    status = []

    if not result:
        print(f"no data: {url}")
        return page_url, status

    for r in result:
        if not isinstance(r, str) or not r.strip():
            print("worng data:", r, type(r))
            continue

        print(r)
        page_url.append((r,))
        status.append(('success', url))

    return page_url, status


conn, cur = connection()

cur.execute("SELECT url FROM urls WHERE status = 'pending'")
data = [i[0] for i in cur.fetchall()]



all_page_url = []
all_status = []

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(process_url, url) for url in data]

    for future in as_completed(futures):
        page_url, status = future.result()

        all_page_url.extend(page_url)
        all_status.extend(status)

        if len(all_page_url) >= 20:
            insert_product_urls(all_page_url)
            update_status(all_status)
            all_page_url.clear()
            all_status.clear()

if all_page_url:
    insert_product_urls(all_page_url)
    update_status(all_status)

conn.close()