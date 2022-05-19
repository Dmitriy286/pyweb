from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from blog.models import Note
from . import serializers

from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.

class NoteListCreateAPIView(APIView):
    def get(self, request: Request) -> Response:
        notes = Note.objects.all()
        return Response([serializers.serialize_note_do_json(note) for note in notes])

    def post(self, request: Request) -> Response:
        data = request.data
        note = Note(title=data["title"])
        note.save(force_insert=True)

        return Response(serializers.serialize_note_created(note), status=status.HTTP_201_CREATED)


class NoteDetailAPIView(APIView):
    def get(self, request: Request, pk) -> Response:
        # note = Note.objects.get(pk)
        note = get_object_or_404(Note, pk=pk)
        return Response(serializers.serialize_note_do_json(note))

    def put(self, request: Request, pk) -> Response:
        note = get_object_or_404(Note, pk=pk)
        data = request.data.get("title")
        note.title = data
        note.save()

        return Response(serializers.serialize_note_do_json(note))

    def delete(self, request: Request, pk) -> Response:
        note = get_object_or_404(Note, pk=pk)
        note.delete()


        return Response(f"Запись: \n {note} \n удалена")
