from django.db import models
from django.contrib.auth.models import User

class News_post(models.Model):
    title = models.CharField('Название новости', max_length=100)
    short_description = models.CharField('Краткое описание новости', max_length=250)
    text = models.TextField('Новость')
    pub_date = models.DateTimeField('Дата публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')  # Связь с пользователем

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
