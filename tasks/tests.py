from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from tasks.models import Task
from django.contrib.auth.models import User
from tasks.serializers import TaskSerializer


class TaskAPITest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="123456")
        self.user2 = User.objects.create_user(username="user2", password="123456")
        self.client.force_authenticate(self.user1)
        self.task = Task.objects.create(
            title="task for test",
            description="this is the description for the test.",
            user=self.user1,
        )
        self.list_create_url = reverse("task-list-create")
        self.detail_url = reverse("task-detail", kwargs={"pk": self.task.id})

    def test_create_task(self):
        data = {"title": "created task", "description": "this is a valid test desc."}
        response = self.client.post(self.list_create_url, data=data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_get_tasks(self):
        response = self.client.get(self.list_create_url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_user_can_get_own_task(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_not_owner_access_to_task(self):
        self.client.force_authenticate(self.user2)
        response = self.client.get(self.detail_url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_update_task(self):
        data = {"title": "new title to work with"}
        response = self.client.put(self.detail_url, data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_delete_task(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
