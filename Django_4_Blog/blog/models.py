from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(
        max_length=250,
        verbose_name='Заголовок',
        help_text='Введите заголовок',
    )
    slug = models.SlugField(max_length=250)
    body = models.TextField(
        'Текст поста',
        help_text='Введите текст поста',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts',
        verbose_name='Автор',
    )
    publish = models.DateTimeField(
        'Дата публикации',
        default=timezone.now,
    )
    created = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        'Дата последнего изменения',
        auto_now=True,
    )
    status = models.CharField(
        'Статус',
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT,
    )

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title
