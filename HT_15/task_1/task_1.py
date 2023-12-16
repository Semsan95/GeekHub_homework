'''
Викорисовуючи requests, написати скрипт, який буде приймати на вхід ID категорії із сайту https://www.sears.com
і буде збирати всі товари із цієї категорії, збирати по ним всі можливі дані (бренд, категорія, модель, ціна, рейтинг тощо)
і зберігати їх у CSV файл (наприклад, якщо категорія має ID 12345, то файл буде називатись 12345_products.csv)
Наприклад, категорія https://www.sears.com/tools-tool-storage/b-1025184 має ІД 1025184
'''

import csv
import requests
import time
from fake_useragent import UserAgent


def get_response(category_id, startindex, endindex):
    ua = UserAgent()
    url = "https://www.sears.com/api/sal/v3/products/search"
    querystring = {
        "startIndex": str(startindex), "endIndex": str(endindex),
        "searchType": "category", "catalogId": "12605", "store": "Sears",
        "storeId": "10153", "zipCode": "10101", "bratRedirectInd": "true",
        "catPredictionInd": "true", "disableBundleInd": "true",
        "filterValueLimit": "500", "includeFiltersInd": "true",
        "shipOrDelivery": "true", "solrxcatRedirection": "true",
        "sortBy": "UNITS_HIGH_TO_LOW", "slimResponseInd": "true",
        "catGroupPath": "Tools|Tool Storage", "catGroupId": category_id
    }

    headers = {
        "authorization": "SEARS",
        "user-agent": ua.random
    }
    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status()
    return response.json()


def csv_headers(category_id):
    with open(f'{category_id}_products', 'w',
              encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Brand', 'Category', 'Model', 'Price', 'Rating'])


def csv_writer(response, category_id):
    with open(f'{category_id}_products', 'a',
              encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        items = response.get('items', [])
        for item_id in range(min(48, len(items))):
            brand = items[item_id].get('brandName')
            category = items[item_id].get('category')
            model = items[item_id].get('name')
            price = items[item_id].get('price', {}).get('finalPriceDisplay')
            rating = items[item_id].get('additionalAttributes', {}).get('rating')
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
            time.sleep(15)
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
