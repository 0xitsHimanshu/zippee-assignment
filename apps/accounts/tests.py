import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
class TestAuth:
    def test_register_user(self):
        client = APIClient()
        data = {
            'email': 'test@example.com',
            'password': 'strongpassword123'
        }
        url = reverse('register')
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.count() == 1
        assert User.objects.get().email == 'test@example.com'

    def test_login_user(self):
        client = APIClient()
        user = User.objects.create_user(email='test@example.com', password='password123')
        data = {
            'email': 'test@example.com',
            'password': 'password123'
        }
        url = reverse('token_obtain_pair')
        response = client.post(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert 'access' in response.data
        assert 'refresh' in response.data
