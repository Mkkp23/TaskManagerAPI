from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskSerializerTest(APITestCase):

    def test_empty_title(self):
        data = {"title": "", "description": "this is the long description."}
        serializer = TaskSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("title", serializer.errors)

    def test_short_description(self):
        data = {"title": "task test", "description": "short des"}
        serializer = TaskSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("description", serializer.errors)


class TaskAPITest(APITestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title="task for test", description="this is the description for the test."
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

    def test_update_task(self):
        data = {"title": "new title to work with"}
        response = self.client.put(self.detail_url, data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_delete_task(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
