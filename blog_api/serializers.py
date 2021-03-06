from rest_framework import serializers

from blog.models import Note, Comment


def serialize_note_to_json(note: Note) -> dict:
    return {
        "id": note.id,
        "title": note.title,
        "message": note.message,
        "public": note.public,
        "author": note.author_id,
    }

def serialize_note_created(note: Note) -> dict:
    return {
        "id": note.id,
        "title": note.title,
        "message": note.message,
        "public": note.public,
        "create_at": note.create_at,
        "update_at": note.update_at,
        "author": note.author_id,
        "smth_else": note.smth_else,
    }

def serialize_comment_to_json(comment: Comment) -> dict:
    return {
        "id": comment.id,
        "note": comment.note_id,
        "rating": comment.get_rating_display(),
        "author": comment.author_id
    }

def serialize_comment_created(comment: Comment) -> dict:
    return {
        "id": comment.id,
        "note": comment.note_id,
        "rating": comment.get_rating_display(),
        "author": comment.author_id
    }

class CommentSerializer(serializers.ModelSerializer):



    class Meta:
        model = Comment
        fields = "__all__"


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        # fields = "__all__"
        exclude = ("public", )
        read_only_fields = ("author", )


class NoteDetailSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    author = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True
    )
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Note
        fields = ("title", "message", "create_at", "update_at",
                  "author", "comment_set")




