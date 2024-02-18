from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from products.models import Product, Category
from django.contrib.auth.models import User


class CartViewSetTestCase(APITestCase):
    def setUp(self):
        category = Category.objects.create(name='Category 1')
        self.product1 = Product.objects.create(name='Product 1', price=100, category=category)
        self.url = reverse('api:cart-list')
        self.admin = User.objects.create_superuser(username='admin', password='adminadmin')
        self.client = APIClient()
        self.client.login(username='admin', password='adminadmin')

    def test_add_product_to_cart(self):
        response = self.client.post(self.url, {'product_id': self.product1.pk}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'status': 'product added to cart'})

    def test_list_cart_items(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_cart_item(self):
        self.test_add_product_to_cart()
        url = reverse('api:cart-detail', kwargs={'pk': self.product1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_remove_product_from_cart(self):
        self.test_add_product_to_cart()
        url = reverse('api:cart-detail', kwargs={'pk': self.product1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'status': 'Product removed from cart'})