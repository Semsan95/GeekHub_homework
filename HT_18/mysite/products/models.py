import requests
import re
from time import sleep
from django.db import models


class Product(models.Model):
    name = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_id = models.TextField(unique=True, editable=False)
    description = models.TextField()
    brand = models.TextField()
    category = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.name

    @classmethod
    def fetch_list(cls, product_ids):
        for product_id in re.split(r', |,| ', product_ids):
            try:
                cls.fetch(product_id)
            finally:
                sleep(40)
    @classmethod
    def fetch(cls, product_id):
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

        details = data['productDetail']['softhardProductdetails'][0]
        category_path = details['hierarchies']['specificHierarchy'][-1]['name']

        try:
            product = cls.objects.get(product_id=product_id)
        except cls.DoesNotExist:
            product = cls(product_id=product_id)
        finally:
            product.name = details['descriptionName']
            product.price = details['salePrice']
            product.description = details['shortDescription']
            product.brand = details['brandName']
            product.category = category_path
            product.link = f'https://www.sears.com{details['seoUrl']}'
            product.save()

        return product