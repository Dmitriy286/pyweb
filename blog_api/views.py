from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from blog.models import Note, Comment
from . import serializers

from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.

class NoteListCreateAPIView(APIView):
    def get(self, request: Request) -> Response:
        notes = Note.objects.all()
        serializer = serializers.NoteSerializer(
            instance=notes,
            many=True
        )
        # return Response([serializers.serialize_note_to_json(note) for note in notes])
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = serializers.NoteSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # serializer.is_valid(raise_exception=True)
        serializer.save() #author=request.user
        return Response(serializer.data, status=status.HTTP_201_CREATED)

        # data = request.data
        # note = Note(title=data["title"])
        # note = Note(**data, author=request.user)
        # note.save(force_insert=True)
        # return Response(serializers.serialize_note_created(note), status=status.HTTP_201_CREATED)

    def delete(self, request: Request) -> Response:
        notes = Note.objects.all()
        notes.delete()

        return Response("Все записи удалены")

class NoteDetailAPIView(APIView):
    def get(self, request: Request, pk) -> Response:
        # # note = Note.objects.get(pk)
        note = get_object_or_404(Note, pk=pk)
        # return Response(serializers.serialize_note_to_json(note))

        # serializer = serializers.NoteSerializer(
        #     instance=note
        # )

        serializer = serializers.NoteDetailSerializer(
            instance=note
        )
        return Response(serializer.data)

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


class NotePublicListAPIView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = serializers.NoteSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(public=True)


class CommentListCreateAPIView(APIView):
    def get(self, request: Request) -> Response:
        comments = Comment.objects.all()
        return Response([serializers.serialize_comment_to_json(comment) for comment in comments])

    def post(self, request: Request) -> Response:
        data = request.data

        # note = Note.objects.get(pk=data["note"])
        # comment = Comment(note=note, rating=data["rating"], author=request.user)

        comment = Comment(note_id=data["note"], rating=data["rating"], author=request.user)
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