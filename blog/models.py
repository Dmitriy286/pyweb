from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=250, verbose_name=_("Заголовок"))
    message = models.TextField(default='', verbose_name="Текст статьи")
    public = models.BooleanField(default=False, verbose_name="Опубликовать")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Время обновления")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # author = models.ForeignKey(User, default=0, on_delete=models.CASCADE)
    smth_else = models.CharField(max_length=5, default='', verbose_name="Что-то еще")


    def __str__(self):
        return f'Заголовок: {self.title}, {self.id}'

    class Meta:
        verbose_name = _("Запись")
        verbose_name_plural = _("Записи")


class Comment(models.Model):
    class Ratings(models.IntegerChoices):
        WITHOUT_RATING = 0, _('Без оценки')
        TERRIBLE = 1, _('Ужасно')
        BADLY = 2, _('Плохо')
        FINE = 3, _('Нормально')
        GOOD = 4, _('Хорошо')
        EXCELLENT = 5, _('Отлично')

