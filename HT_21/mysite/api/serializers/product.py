from rest_framework import serializers
from products.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = (
            'id',
            'name', 
            'price', 
            'product_id', 
            'description', 
            'brand', 
            'category', 
            'link'
        )