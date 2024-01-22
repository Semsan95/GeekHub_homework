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
