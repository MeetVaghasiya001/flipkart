from request_data import request
import json
import gzip
import hashlib

def add_page_save(page, name):
    folder_path = 'C:/Users/meet.vaghasiya/Desktop/bif files/flipkart'
    with gzip.open(f'{folder_path}/{name}.json.gz', 'wt', encoding='utf-8') as f:
        json.dump(page, f, indent=4, default=str)


def all_filters(api, params):
    data = request(api, params)

    filters = {}
    slots = data.get('RESPONSE', {}).get('slots', [])

    for s in slots:
        if s.get('widget', {}).get('type') != 'FILTERS':
            continue

        facets = s.get('widget', {}).get('data', {}).get('filters', {}).get('facetResponse', {}).get('facets', [])

        for f in facets:
            if f.get('id') == 'price_range':
                keys = [
                    v.get('key')
                    for g in f.get('values', [])
                    for v in g.get('values', [])
                    if v.get('key') is not None
                ]

                ranges = [(keys[i], keys[i+1]) for i in range(len(keys)-1)]

                filters['price'] = [
                    (f"facets.price_range.from={a}", f"facets.price_range.to={b}")
                    for a, b in ranges
                ]
                continue

            title = f.get('title')
            if title:
                filters[title] = [
                    v.get('resource', {}).get('params')
                    for g in f.get('values', [])
                    for v in g.get('values', [])
                    if v.get('resource', {}).get('params')
                ]

    with open('filters.json', 'w', encoding='utf-8') as f:
        json.dump(filters, f, indent=4, ensure_ascii=False)

    return filters


local_unique = set()

def featch_urls(url):
    global local_unique
    json_data = {
        'pageUri': url,
        'pageContext': {
            'fetchSeoData': True,
            'paginatedFetch': False,
            'pageNumber': 1,
        },
        'requestContext': {
            'type': 'BROWSE_PAGE',
            'ssid': '1n34lds3c00000001778153277507',
            'sqid': 'to0gglu6o00000001778153308102',
        },
    }

    page_urls = []
    
    count=0
    while True:
        if int(json_data['pageContext']['pageNumber']) <=25:
            count+=1
            response = request('https://1.rome.api.flipkart.com/api/4/page/fetch', json_data)

            if not response:
                break

            data = url + f"page={json_data['pageContext']['pageNumber']}"
            hash_url = hashlib.sha256(data.encode()).hexdigest()
            add_page_save(response, hash_url)

            main_path = response.get('RESPONSE', {}).get('pageData', {}).get('seoData', {}).get('schema')
            if not main_path:
                break

            for item in main_path:
                if item.get('@type') != 'ItemList':
                    continue

                elements = item.get('itemListElement')
                if not elements:
                    break

                for u in elements:
                    product_url = u.get('url')
                    if not product_url:
                        continue
                    if product_url not in local_unique:
                        local_unique.add(product_url)
                        page_urls.append(product_url)
                        
                    else:
                        print('already have')
            print(int(json_data['pageContext']['pageNumber']))
            json_data['pageContext']['pageNumber'] = str(int(json_data['pageContext']['pageNumber']) + 1)
        else:
            break
    return page_urls


# data = featch_urls('https://www.flipkart.com/search?q=t+shirt&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p[]=facets.brand%255B%255D%3DPUMA')
# with open('clean.json','w',encoding='utf-8') as f:
#     json.dump(data,f,indent=4,default=str)