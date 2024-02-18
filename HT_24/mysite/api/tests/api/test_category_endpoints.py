from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .factories import CategoryFactory
from django.urls import reverse
from rest_framework import status

class CategoryViewSetTestCase(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(username='admin', password='adminadmin')
        self.client = APIClient()
        self.client.login(username='admin', password='adminadmin')
        self.category = CategoryFactory.create()
        self.url = reverse('api:category-list')
        
    def test_list_categories(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_retrieve_category(self):
        url = reverse('api:category-detail', kwargs={'pk': self.category.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_category(self):
        data = {
            'name': 'New Category'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_update_category(self):
        url = reverse('api:category-detail', kwargs={'pk': self.category.pk})
        data = {
            'name': 'Updated Category'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_delete_category(self):
        url = reverse('api:category-detail', kwargs={'pk': self.category.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)