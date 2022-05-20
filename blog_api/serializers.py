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
        "note": comment.note,
        "author": comment.rating,
    }

def serialize_comment_created(comment: Comment) -> dict:
    return {
        "id": comment.id,
        "note": comment.note,
        "author": comment.rating,
    }



