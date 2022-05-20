from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from blog.models import Note, Comment
from . import serializers

from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.

class NoteListCreateAPIView(APIView):
    def get(self, request: Request) -> Response:
        notes = Note.objects.all()
        return Response([serializers.serialize_note_to_json(note) for note in notes])

    def post(self, request: Request) -> Response:
        data = request.data
        # note = Note(title=data["title"])
        note = Note(**data, author=request.user)
        note.save(force_insert=True)

        return Response(serializers.serialize_note_created(note), status=status.HTTP_201_CREATED)


class NoteDetailAPIView(APIView):
    def get(self, request: Request, pk) -> Response:
        # note = Note.objects.get(pk)
        note = get_object_or_404(Note, pk=pk)
        return Response(serializers.serialize_note_to_json(note))

    def put(self, request: Request, pk) -> Response:
        note = get_object_or_404(Note, pk=pk)
        data = request.data.get("title")
        note.title = data
        note.save()

        return Response(serializers.serialize_note_to_json(note))

    def delete(self, request: Request, pk) -> Response:
        note = get_object_or_404(Note, pk=pk)
        note.delete()


        return Response(f"Запись: \n {note} \n удалена")


class CommentListCreateAPIView(APIView):
    def get(self, request: Request) -> Response:
        comments = Comment.objects.all()
        return Response([serializers.serialize_comment_to_json(comment) for comment in comments])

    def post(self, request: Request) -> Response:
        data = request.data
        # comment = Comment(author=data["author"], note=data["note"], rating=data["rating"])
        comment = Comment(**data, author=request.user)
        comment.save(force_insert=True)

        return Response(serializers.serialize_comment_created(comment), status=status.HTTP_201_CREATED)


class CommentDetailAPIView(APIView):
    def get(self, request: Request, pk) -> Response:

        comment = get_object_or_404(Comment, pk=pk)
        return Response(serializers.serialize_comment_to_json(comment))

    def put(self, request: Request, pk) -> Response:
        comment = get_object_or_404(Comment, pk=pk)
        author_data = request.data.get("author")
        note_data = request.data.get("note")
        rating_data = request.data.get("rating")

        comment.author = author_data
        comment.note = note_data
        comment.rating = rating_data
        comment.save()

        return Response(serializers.serialize_comment_to_json(comment))