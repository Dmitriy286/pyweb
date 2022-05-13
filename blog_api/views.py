from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request

from blog.models import Note

from django.shortcuts import get_object_or_404

# Create your views here.

class NoteListCreateAPIView(APIView):
    def get(self, request: Request) -> Request:
        notes = Note.objects.all()
        return Request(notes)

    def post(self, request: Request) -> Request:






class NoteDetailAPIView
