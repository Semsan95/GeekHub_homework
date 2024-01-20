from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_id = models.CharField(max_length=50, unique=True, editable=False)
    description = models.TextField()
    brand = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    link = models.URLField()

    def __str__(self):
        return self.name

    @classmethod
    def create_or_update_product(cls, product_id, product_data):

        try:
            product = cls.objects.get(product_id=product_id)
        except cls.DoesNotExist:
            product = cls(product_id=product_id)
        finally:
            product.name = product_data['name']
            product.price = float(product_data['price'])
            product.description = product_data['description']
            product.brand = product_data['brand']
            product.category = product_data['category']
            product.link = product_data['link']
            product.save()

        return product
    
