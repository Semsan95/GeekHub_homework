from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from products.models import Category
from .factories import ProductFactory
from django.contrib.auth.models import User
 

class ProductViewSetTestCase(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(username='admin', password='adminadmin')
        self.client = APIClient()
        self.client.login(username='admin', password='adminadmin')
        self.product = ProductFactory.create()
        self.url = reverse('api:product-list')

    def test_list_products(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_product(self):
        url = reverse('api:product-detail', kwargs={'pk': self.product.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        category = Category.objects.create(name='New Category')
        data = {
            'name': 'New Product',
            'price': 100.00,
            'description': 'This is a new product',
            'brand': 'New Brand',
            'category': category.pk,
            'link': 'http://newproduct.com'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_product(self):
        url = reverse('api:product-detail', kwargs={'pk': self.product.pk})
        data = {
            'name': 'Updated Product',
            'price': 200.00,
            'description': 'Updated description',
            'brand': 'Updated Brand',
            'category': self.product.category.pk,
            'link': 'http://updatedproduct.com'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_product(self):
        url = reverse('api:product-detail', kwargs={'pk': self.product.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)