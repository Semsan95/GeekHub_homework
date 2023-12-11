'''
Викорисовуючи requests, написати скрипт, який буде приймати на вхід ID категорії із сайту https://www.sears.com
і буде збирати всі товари із цієї категорії, збирати по ним всі можливі дані (бренд, категорія, модель, ціна, рейтинг тощо)
і зберігати їх у CSV файл (наприклад, якщо категорія має ID 12345, то файл буде називатись 12345_products.csv)
Наприклад, категорія https://www.sears.com/tools-tool-storage/b-1025184 має ІД 1025184
'''

import csv
import requests
import time

def get_response(category_id, startindex, endindex):
    url = "https://www.sears.com/api/sal/v3/products/search"
    querystring = {
        "startIndex": str(startindex), "endIndex": str(endindex), "searchType": "category", "catalogId": "12605", "store": "Sears",
        "storeId": "10153", "zipCode": "10101", "bratRedirectInd": "true", "catPredictionInd": "true",
        "disableBundleInd": "true", "filterValueLimit": "500", "includeFiltersInd": "true", "shipOrDelivery": "true",
        "solrxcatRedirection": "true", "sortBy": "UNITS_HIGH_TO_LOW", "whiteListCacheLoad": "false",
        "eagerCacheLoad": "true", "slimResponseInd": "true", "catGroupPath": "Tools|Tool Storage", "catGroupId": category_id
    }
    headers = {
        "cookie": "_gid=GA1.2.807226593.1702034316; zipCode=10101; city=New York; state=NY; irp=0cdac275-2742-4103-810f-ab1af84c9256|SMa7MQu8TI%2ByZ6mNeZMOj2dFjINqbx%2Br%2BAP5qJ4d5eY%3D|G|5950e5a3-f6c2-46f2-ab47-eccdc9845120|0|NO_SESSION_TOKEN_COOKIE; initialTrafficSource=utmcsr=(direct)|utmcmd=(none)|utmccn=(not set); __utmzzses=1; _gcl_au=1.1.430131765.1702034318; ltkSubscriber-Footer=eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCJ9; _clck=kiuw4f%7C2%7Cfhd%7C0%7C1437; GSIDNqXoacKY53MN=199e906a-3eb4-4066-8e3c-5e284e405986; STSID974004=c44eea8a-cb35-4af1-beb7-de159099188d; cookie=0e2f4250-41c1-449f-9ba0-c81d61b900a3; cookie_cst=zix7LPQsHA%3D%3D; __qca=P0-725134470-1702034318891; __gsas=ID=a3bb7136ad3cbfca:T=1702034331:RT=1702034331:S=ALNI_MaiJ8i4kef_hEj-T2ZXflC1DYyTHg; _pbjs_userid_consent_data=3524755945110770; _sharedid=32f83bc7-d362-404c-af42-671e7b4ca4de; _lr_env_src_ats=false; __pr.3q8y1p=xWGmgeDN4_; _fbp=fb.1.1702044655358.18119962; _li_dcdm_c=.sears.com; _lc2_fpi=ec742730c587--01hh4w8rfs85p968js2rwnn8fh; _lc2_fpi_meta={%22w%22:1702044656122}; __gads=ID=9d1a5fc96e196086:T=1702044656:RT=1702044656:S=ALNI_MacaLMXPoaqYgIupIJeJlqJ6FhvQA; _li_ss=Ck8KBQgKENcWCgYI3QEQ0xYKBQgGENcWCgYIpQEQ1xYKBgiBARDXFgoFCAwQ2BYKBgiiARDXFgoJCP____8HENgWCgUICxDXFgoGCNIBENcW; _li_ss_meta={%22w%22:1702044658447%2C%22e%22:1704636658447}; ftr_ncd=6; ltkpopup-session-depth=7-11; ftr_blst_1h=1702054907611; __cf_bm=j5jY4Bm4ymUl4u5vmO3jQTqRilgHC3dQfYVaLxXycao-1702058340-0-AeySexliSL9urouvxfD8qTtawHMIeMXZ3++O+03hoE3PJSywItQx2tfL6dR+/L4RVWeLb+xyb3fgeVidrdrOD5BQXvi1t1F8hDtcUwBvcsov; cf_clearance=gQNiEkuCyOFa6yfi7Sjzjcs3bmlnuqpyKSrgivXCF0E-1702058367-0-1-80ac5f4c.64e46eef.1432cd6f-0.2.1702058367; OptanonAlertBoxClosed=2023-12-08T17:59:27.490Z; _ga=GA1.1.223341688.1702034316; OptanonConsent=isIABGlobal=false&datestamp=Fri+Dec+08+2023+19%3A59%3A28+GMT%2B0200+(%D0%B7%D0%B0+%D1%81%D1%85%D1%96%D0%B4%D0%BD%D0%BE%D1%94%D0%B2%D1%80%D0%BE%D0%BF%D0%B5%D0%B9%D1%81%D1%8C%D0%BA%D0%B8%D0%BC+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%B8%D0%BC+%D1%87%D0%B0%D1%81%D0%BE%D0%BC)&version=202209.1.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1%2CSPD_BG%3A1&geolocation=UA%3B26&AwaitingReconsent=false; _uetsid=88c4ad8095bb11ee964351e1e70058b7; _uetvid=88c4f70095bb11eea7b899b1300e4830; forterToken=e300ecb5117a4687ab524b37a99b1995_1702058365315_379_UDF43-m4_13ck; cto_bundle=O4YTkF9rejQ5bHlIeXRHbVdsMmJ3ZGRNWTNiZWdwbSUyQnc3SmR4THBEYmRpRHBYblJzT0pvbkhheGZOVnhIam95ZnVVYTMwQlllZDIwc0tSQXBDTm1CR2pTMXpUWjJVTlVPWE8yNncxcllFN2hnZElocEZpclluN1BhJTJCOTVTVlZXZmNXSGllU3oyckZlUTlZekdYMEZTVk5GVzB3JTNEJTNE; cto_bidid=LW3lJ19sSFliayUyRkxxVFROZm50MDdtU3lmZWU1ZyUyRklETnpRVVM3S3lFSFJzb1JDUGFUUGI0VHR3VEZCYXRFcCUyQlF0RGxSUE45YlpXWE5ObHdFMXBhSzZTbE54WDFSM3M4JTJGZVE2WE1JalU5Q3ZudXhRJTNE; _ga_L7QE48HF7H=GS1.1.1702054397.6.1.1702058424.60.0.0",
        "authority": "www.sears.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "uk,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
        "authorization": "SEARS",
        "content-type": "application/json",
        "dnt": "1",
        "referer": "https://www.sears.com/tools-tool-storage/b-1025184?subCatView=true&sortOption=UNITS_HIGH_TO_LOW&adcell=Tools_VisNav_ToolStorage",
        "sec-ch-ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status()
    return response.json()


def csv_headers(category_id):
    with open(f'{category_id}_products', 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Brand', 'Category', 'Model', 'Price', 'Rating'])


def csv_writer(response, category_id):
    with open(f'{category_id}_products', 'a', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for item_id in range(0, 48):
            brand = response['items'][item_id]['brandName']
            category = response['items'][item_id]['category']
            model = response['items'][item_id]['name']
            price = response['items'][item_id]['price']['finalPriceDisplay']
            rating = response['items'][item_id]['additionalAttributes']['rating']
            writer.writerow([brand, category, model, price, rating])


def user_input():
    category_id = input('Введіть ID потрібної категорії: ')
    return category_id


def start_end_generator():
    start = 1
    end = 48
    while True:
        yield start, end
        start += 48
        end += 48

def start():
    category_id = user_input()
    csv_headers(category_id)
    for startindex, endindex in start_end_generator():
        try:
            response = get_response(category_id, startindex, endindex)
            csv_writer(response, category_id)
            print(f'Внесено товари від {startindex} до {endindex}.')
            time.sleep(30)
        except requests.exceptions.HTTPError as err:
            print(f"Помилка HTTP: {err}")
            print('Роботу завершено.')
            break
        except requests.exceptions.RequestException as e:
            print(f'Помилка запиту: {e}')
            print('Роботу завершено.')
            break
        except Exception as e:
            print(f'Невідома помилка: {e}')
            print('Роботу завершено.')
            break

start()



