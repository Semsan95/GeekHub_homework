import requests
import re
from time import sleep
from products.models import Product

def fetch_product(product_id, Product):
    url = f"https://www.sears.com/api/sal/v3/products/details/{product_id}"
    headers = {
        'authorization': 'SEARS',
    }
    params = {
        "storeName": "Sears",
        "memberStatus": "G",
        "zipCode": "10101"
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    product_data = {
        'name': data['productDetail']['softhardProductdetails'][0]['descriptionName'],
        'price': data['productDetail']['softhardProductdetails'][0]['salePrice'],
        'product_id': product_id,
        'description': data['productDetail']['softhardProductdetails'][0]['shortDescription'],
        'brand': data['productDetail']['softhardProductdetails'][0]['brandName'],
        'category': data['productDetail']['softhardProductdetails'][0]['hierarchies']['specificHierarchy'][-1]['name'],
        'link': f'https://www.sears.com{data['productDetail']['softhardProductdetails'][0]['seoUrl']}'
    }

    product = Product.create_or_update_product(product_id, product_data)

    return product

def fetch_product_list(product_ids, Product):
    for product_id in re.split(r', |,| ', product_ids):
        try:
            fetch_product(product_id, Product)
        finally:
            sleep(40)