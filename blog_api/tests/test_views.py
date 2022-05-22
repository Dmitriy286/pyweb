import unittest
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.utils import json

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
        new_title = "test_title"
        url = "/notes/"
        data = {
            "title": new_title,
            "author": 1
        }
        resp = self.client.post(url, json.dumps(data), content_type="application/json")
        # json.dumps(data)
        # self.response = self.c.post('/pipeline-endpoint', json_data, content_type="application/json")
        expected_status_code = status.HTTP_201_CREATED
        self.assertEqual(expected_status_code, resp.status_code)
        expected_title = new_title
        self.assertEqual(expected_title, resp.data["title"])

    def test_delete_all(self):
        Note.objects.create(title="Test title", author_id=1)
        test_user = User.objects.get(username="test@test.ru")
        Note.objects.create(title="Test title", author=test_user)

        url = "/notes/"
        resp = self.client.get(url)
        response_data = resp.data
        self.assertEqual(2, len(response_data))

        resp = self.client.delete(url)
        # expected_response = "Все записи удалены"
        # self.assertEqual(expected_response, resp)

        resp = self.client.get(url)
        response_data = resp.data
        self.assertEqual(0, len(response_data))
        self.assertEqual([], response_data)



class TestNoteDetailAPIView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username="test@test.ru")
        test_user = User.objects.get(username="test@test.ru")
        new_title = "Test title"
        Note.objects.create(title=new_title, author=test_user)


    def test_object_view(self):
        # test_user = User.objects.get(username="test@test.ru")
        # new_title = "Test title"
        # note = Note.objects.create(title=new_title, author=test_user)
        note_pk = 1
        url = f"/notes/{note_pk}/"
        resp = self.client.get(url)
        expected_status_code = status.HTTP_200_OK
        self.assertEqual(expected_status_code, resp.status_code)

        response_data = resp.data
        # self.assertEqual(note.title, response_data["title"])
        # self.assertEqual(note.id, response_data["id"])
        data = {
            "id": 1,
            "title": "Test title",
            "message": "",
            "public": False,
            "author": 1
        }
        self.assertDictEqual(data, response_data)


    def test_object_does_not_exist_view(self):
        url = "/notes/10/"
        resp = self.client.get(url)
        expected_status_code = status.HTTP_404_NOT_FOUND
        self.assertEqual(expected_status_code, resp.status_code)

    def test_update_object_view(self):
        test_user = User.objects.get(username="test@test.ru")
        title = "Test title"
        new_title = "New title"
        note_pk = 1
        url = f"/notes/{note_pk}/"
        new_data = {
            "title": new_title,
        }
        resp = self.client.put(url, json.dumps(new_data), content_type="application/json")
        expected_status_code = status.HTTP_200_OK
        self.assertEqual(expected_status_code, resp.status_code)
        self.assertEqual(new_data["title"], resp.data["title"])

    def test_update_does_not_exist_view(self):
        url = "/notes/1/"
        new_title = "New title"
        new_data = {
            "title": new_title,
        }
        resp = self.client.put(url, json.dumps(new_data), content_type="application/json")
        expected_status_code = status.HTTP_404_NOT_FOUND
        self.assertEqual(expected_status_code, resp.status_code)