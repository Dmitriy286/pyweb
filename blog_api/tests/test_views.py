from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

from blog.models import Note

class TestNoteListCreateAPIView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username="test@test.ru")

    def test_empty_list_objects(self):
        url = "/notes/"
        resp = self.client.get(url)
        expected_status_code = status.HTTP_200_OK
        self.assertEqual(expected_status_code, resp.status_code)

        response_data = resp.data
        expected_data = []
        self.assertEqual(response_data, expected_data)

    def test_list_objects(self):
        Note.objects.create(title="Test title", author_id=1)
        test_user = User.objects.get(username="test@test.ru")
        Note.objects.create(title="Test title", author=test_user)

        url = "/notes/"
        resp = self.client.get(url)
        expected_status_code = status.HTTP_200_OK
        self.assertEqual(expected_status_code, resp.status_code)

        response_data = resp.data
        self.assertEqual(2, len(response_data))

    def test_create_object(self):

        ...


class TestNoteDetailAPIView(APITestCase):
    ...