"""Модели приложения Account."""


from django.db import models
from django.conf import settings


class Profile(models.Model):
    """Расширение стандартной модели Юзер."""

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                verbose_name='Имя пользователя')
    date_of_birth = models.DateField('Дата рождения:',
                                     null=True, blank=True)
    photo = models.ImageField('Аватар', upload_to='users/%Y/%m/%d',
                              blank=True)

    class Meta:
        """Класс мета модели профиля."""

        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        """Возвращает имя объекта модели."""
        return f'Профиль {self.user.username}'
