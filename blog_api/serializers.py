from blog.models import Note


def serialize_note_do_json(note: Note) -> dict:
    return {
        "title": note.title,
        "message": note.message,
        "public": note.public,
        "create_at": note.create_at,
        "update_at": note.update_at,
    }

def serialize_note_created(note: Note) -> dict:
    return {
        "title": note.title,
        "message": note.message,
        "public": note.public,
        "create_at": note.create_at,
        "update_at": note.update_at,
    }
