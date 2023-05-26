"""Модели для приложения Images."""

from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Image(models.Model):
    """Модель Image для приложения Images."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='images_created',
                             on_delete=models.CASCADE,
                             verbose_name='Автор')
    title = models.CharField(max_length=200,
                             verbose_name='Название')
    slug = models.SlugField(max_length=200,
                            blank=True)
    url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to='images/%Y/%m/%d',
                              verbose_name='Изображение')
    description = models.TextField(blank=True,
                                   verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата создания')
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='images_liked',
                                        blank=True)

    class Meta:
        """Класс мета модели Image."""

    indexes = [
        models.Index(fields=['-created'])
    ]
    ordering = ['-created']
    verbose_name = 'Картинка'
    verbose_name_plural = 'Картинки'

    def __str__(self):
        """Возвращает имя объекта картинки.."""
        return self.title

    def save(self, *args, **kwargs):
        """Автослагифаер при его отсутствие.0"""
        if not self.slug:
            self.slug = slugify(self.title)
        super.save(*args, **kwargs)
