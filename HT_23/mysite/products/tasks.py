from mysite.celery import app
from products.models import Product
from services.parsers import fetch_product_list

@app.task(name="products_fetch")
def fetch_products_task(product_ids):
    fetch_product_list(product_ids)
    return Product.objects.count()