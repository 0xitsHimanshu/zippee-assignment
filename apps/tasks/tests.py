import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apps.tasks.models import Task
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
class TestTasks:
    @pytest.fixture
    def user(self):
        return User.objects.create_user(email='test@example.com', password='password')

    @pytest.fixture
    def client(self, user):
        client = APIClient()
        client.force_authenticate(user=user)
        return client

    def test_create_task(self, client, user):
        url = reverse('task-list')
        data = {'title': 'New Task'}
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Task.objects.count() == 1
        assert Task.objects.get().user == user

    def test_get_tasks(self, client, user):
        Task.objects.create(title='Task 1', user=user)
        url = reverse('task-list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1

    def test_update_task(self, client, user):
        task = Task.objects.create(title='Task 1', user=user)
        url = reverse('task-detail', args=[task.id])
        data = {'title': 'Updated Task', 'completed': True}
        response = client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        task.refresh_from_db()
        assert task.title == 'Updated Task'
        assert task.completed is True

    def test_delete_task(self, client, user):
        task = Task.objects.create(title='Task 1', user=user)
        url = reverse('task-detail', args=[task.id])
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Task.objects.count() == 0
