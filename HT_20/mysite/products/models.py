from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_id = models.CharField(max_length=50, unique=True, editable=False)
    description = models.TextField()
    brand = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
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
            product.category = Category.objects.get_or_create(name=product_data['category'])[0]
            product.link = product_data['link']
            product.save()

        return product
    
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name