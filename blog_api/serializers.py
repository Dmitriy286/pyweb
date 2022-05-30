from datetime import datetime

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
    rating = serializers.SerializerMethodField('get_rating')

    def get_rating(self, obj: Comment):
        return {
            'value': obj.rating,
            'display': obj.get_rating_display()
        }

    author = serializers.SerializerMethodField('get_author')

    def get_author(self, obj: Comment):
        return {
            'value': obj.author_id,
            'display': f'Author with ID: {obj.author_id}'
        }

    class Meta:
        model = Comment
        fields = "__all__"


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"
        # exclude = ("public", )
        read_only_fields = ("author", )

class NotePublicSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Note
        read_only_fields = ("author",)
        fields = ("title", "message", "create_at", "update_at", "public",
                  "author", "comments")




class NoteDetailSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    author = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True
    )
    comments = CommentSerializer(many=True, read_only=True)
    # create_at = serializers.DateField()

    class Meta:
        model = Note
        fields = ("title", "message", "create_at", "update_at",
                  "author", "comments")

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        create_at = datetime.strptime(ret['create_at'], '%Y-%m-%dT%H:%M:%S.%f')
        ret['create_at'] = create_at.strftime('%d %B %Y %H:%M')

        return ret


