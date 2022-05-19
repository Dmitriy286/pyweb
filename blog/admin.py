from django.contrib import admin

from .models import Note

# Register your models here.
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'public')

    fields = (('title', 'public'), ('update_at', 'create_at'), 'message', 'author')

    readonly_fields = ['update_at', 'create_at']

    search_fields = ('title', 'id')

    search_help_text = "Ищите"

    list_filter = ['public']

