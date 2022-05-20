import unittest
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django import TestCase

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

    # @unittest.skip("Еще не реализовано")
    def test_create_object(self):
        new_title = "test_title"
        data = {
            "title": new_title
        }
        url = "/notes/"
        # resp = self.client.post(url, data=data, content_type="application/json") #todo doesn't work
        # self.assertEqual(status.HTTP_200_OK, resp.status_code)
        # note = Note.objects.get(title=new_title)

        # Note.objects.get(title=new_title) #self.assertTrue(Note.objects.exists(title=new_title))

        note1 = Note.objects.get(title=new_title, author="qwerty")
        wrong_data = {
            "title": new_title,
            "author": "qwerty"
        }
        resp = self.client.post(url, data=wrong_data, content_type="application/json")
        expected_status_code = status.HTTP_201_CREATED
        self.assertEqual(expected_status_code, resp.status_code)


class TestNoteDetailAPIView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username="test@test.ru")

    def test_object_view(self):
        test_user = User.objects.get(username="test@test.ru")
        new_title = "Test title"
        note = Note.objects.create(title=new_title, author=test_user)

        url = "/notes/1/"
        resp = self.client.get(url)
        expected_status_code = status.HTTP_200_OK
        self.assertEqual(expected_status_code, resp.status_code)

        response_data = resp.data
        self.assertEqual(note.title, resp.data["title"])
        self.assertEqual(note.id, resp.data["id"])
        # self.assertTrue(Note.objects.exists(title=new_title))
