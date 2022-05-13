from django.db import models


# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=250, verbose_name="Заголовок")
    message = models.TextField(default='', verbose_name="Текст статьи")
    public = models.BooleanField(default=False, verbose_name="Опубликовать")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Время обновления")

    def __str__(self):
        return f'Заголовок: {self.title}'
