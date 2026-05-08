import requests
import json

def request(url,json_data = None):
    cookies = {
        'T': 'TI177425845081000132535124261580315770554419894005481129429981510333',
        'K-ACTION': 'null',
        'dpr': '1.5',
        'rt': 'null',
        'vh': '584',
        'vw': '1274',
        'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE3Nzk4NjM2NzUsImlhdCI6MTc3ODEzNTY3NSwiaXNzIjoia2V2bGFyIiwianRpIjoiZWM2ZThlNGQtMjE3ZC00M2M3LWI1ZTAtNWI5MTY0NzJhMTU4IiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzc0MjU4NDUwODEwMDAxMzI1MzUxMjQyNjE1ODAzMTU3NzA1NTQ0MTk4OTQwMDU0ODExMjk0Mjk5ODE1MTAzMzMiLCJrZXZJZCI6IlZJRTYyNzBCMDE4NUUyNDMzRDk4NERGRTQwOUJDMDU0MEYiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6M30.BQqWAT81ZYTIZ7OW5aS_HKowGXeEGaQ4S3pKeyudR64',
        'Network-Type': '4g',
        'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1',
        'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C20581%7CMCMID%7C09469107191527221813551563858343731764%7CMCAAMLH-1778560777%7C12%7CMCAAMB-1778740527%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1778142927s%7CNONE%7CMCAID%7CNONE',
        '_gcl_au': '1.1.1336840447.1778135736',
        'vd': 'VIE6270B0185E2433D984DFE409BC0540F-1774258459866-19.1778138158.1778135676.156800938',
        's_sq': 'flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Asearch%2526pidt%253D1%2526oid%253DfunctionJr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DDIV',
        'ud': '2.VogYwlUWqZC3mok_5Tvo2stTYjZu5u2qDbEYJRpeUrEiIztHA4giwD8hAU652G1fN98NEfGdmpc_m5j4DAcjYFDt4noLNOHCQ0DQVPngntipiNi960XiSjqoREMp8wwtt74DpAQh3VzxuduwT7NCJxIuBSTCDVa0O6IXOmsks-HWO17J8sjdc4BLu2ZmFhaP8otkOZmElhShJUzlYD-2KouFMyvPbzu1smtMnbxRA--9OdJJDAUHRr2m-4jzczpSb5Y8rPdoUXGfgnwO6PkS20xuhO6LzeISs07nzrGyy3M81RFGEXzdPwwt1LSkz5AhXk8J4yi8rV5A4cwvkFF-3UCNZ3mnhBN-UmZg9_m_4C-jW-zETv6S64fjCONo9CpVYjRHbLewIPSvdGxEZ2B-cGQ_96_mGY71kFif8nNg-CcPPolZKXRpWSN3IBa_Qz_rkEv0TFA89LcFooX3CTxg2q6nOkE8QLkkyT_DEF25enLyNjx3dQH_J-tpgzrZ1B2v-L0p-gPKkIkTtD80mwKszTwalZ5dKUkctNla39O05wpWwFCHISQLxZ0FwAsWJiUe',
        'S': 'd1t16PT9uPz9LFj8/SlgeCz83HMGHgUZbSf2xnkr3I5RHWRsIgO6m/ouo/sm0qyAb+F1cSKvNrMwjTIjbnceFXeVYBg==',
        'SN': 'VIE6270B0185E2433D984DFE409BC0540F.TOK76F970370A80480696939C3C02663E59.1778138199388.LO',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://www.flipkart.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.flipkart.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        'X-User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 FKUA/website/42/website/Desktop',
        'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        # 'Cookie': 'T=TI177425845081000132535124261580315770554419894005481129429981510333; K-ACTION=null; dpr=1.5; rt=null; vh=584; vw=1274; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE3Nzk4NjM2NzUsImlhdCI6MTc3ODEzNTY3NSwiaXNzIjoia2V2bGFyIiwianRpIjoiZWM2ZThlNGQtMjE3ZC00M2M3LWI1ZTAtNWI5MTY0NzJhMTU4IiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzc0MjU4NDUwODEwMDAxMzI1MzUxMjQyNjE1ODAzMTU3NzA1NTQ0MTk4OTQwMDU0ODExMjk0Mjk5ODE1MTAzMzMiLCJrZXZJZCI6IlZJRTYyNzBCMDE4NUUyNDMzRDk4NERGRTQwOUJDMDU0MEYiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6M30.BQqWAT81ZYTIZ7OW5aS_HKowGXeEGaQ4S3pKeyudR64; Network-Type=4g; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C20581%7CMCMID%7C09469107191527221813551563858343731764%7CMCAAMLH-1778560777%7C12%7CMCAAMB-1778740527%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1778142927s%7CNONE%7CMCAID%7CNONE; _gcl_au=1.1.1336840447.1778135736; vd=VIE6270B0185E2433D984DFE409BC0540F-1774258459866-19.1778138158.1778135676.156800938; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Asearch%2526pidt%253D1%2526oid%253DfunctionJr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DDIV; ud=2.VogYwlUWqZC3mok_5Tvo2stTYjZu5u2qDbEYJRpeUrEiIztHA4giwD8hAU652G1fN98NEfGdmpc_m5j4DAcjYFDt4noLNOHCQ0DQVPngntipiNi960XiSjqoREMp8wwtt74DpAQh3VzxuduwT7NCJxIuBSTCDVa0O6IXOmsks-HWO17J8sjdc4BLu2ZmFhaP8otkOZmElhShJUzlYD-2KouFMyvPbzu1smtMnbxRA--9OdJJDAUHRr2m-4jzczpSb5Y8rPdoUXGfgnwO6PkS20xuhO6LzeISs07nzrGyy3M81RFGEXzdPwwt1LSkz5AhXk8J4yi8rV5A4cwvkFF-3UCNZ3mnhBN-UmZg9_m_4C-jW-zETv6S64fjCONo9CpVYjRHbLewIPSvdGxEZ2B-cGQ_96_mGY71kFif8nNg-CcPPolZKXRpWSN3IBa_Qz_rkEv0TFA89LcFooX3CTxg2q6nOkE8QLkkyT_DEF25enLyNjx3dQH_J-tpgzrZ1B2v-L0p-gPKkIkTtD80mwKszTwalZ5dKUkctNla39O05wpWwFCHISQLxZ0FwAsWJiUe; S=d1t16PT9uPz9LFj8/SlgeCz83HMGHgUZbSf2xnkr3I5RHWRsIgO6m/ouo/sm0qyAb+F1cSKvNrMwjTIjbnceFXeVYBg==; SN=VIE6270B0185E2433D984DFE409BC0540F.TOK76F970370A80480696939C3C02663E59.1778138199388.LO',
    }
    proxies = {
        'http': 'http://ycclsgto:klygdc9rt4ep@31.59.20.176:6754',
        'https': 'http://ycclsgto:klygdc9rt4ep@31.59.20.176:6754',
    }

    

    response = requests.post(url, cookies=cookies, headers=headers, json=json_data,proxies=proxies)

    if response.status_code == 200:
        with open('product.json','w',encoding='utf-8') as f:
            json.dump(response.json(),f,indent=4,ensure_ascii=False)
        return response.json()
    else:
        print(response.status_code)
        print(response.text)
        return None