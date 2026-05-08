from parser import *
from urllib.parse import quote_plus
from db import *


create_db()
def build_url(param, search):
    base = f"https://www.flipkart.com/search/search?q={quote_plus(search)}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

    if isinstance(param, tuple):
        return base + "".join(f"&p[]={quote_plus(p)}" for p in param)

    return base + f"&p[]={quote_plus(param)}"


search = "t shirt"
json_data = {
        'pageUri': f'/search?q={search}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off',
        'pageContext': {
            'fetchSeoData': True, 
            'paginatedFetch': False, 
            'pageNumber': 1
            },
        'requestContext': {
            'type': 'BROWSE_PAGE'
            }
    }

all_links = all_filters("https://1.rome.api.flipkart.com/api/4/page/fetch", json_data)

all_filters_url = [
    item
    for values in all_links.values()
    if isinstance(values, list)
    for item in values
]

full_urls = [build_url(p, search) for p in all_filters_url]


row = []
for i in full_urls:
    row.append((i,))
    if len(row) == 20:
        insert_urls(row)
        row.clear()

if row:
    insert_urls(row)
