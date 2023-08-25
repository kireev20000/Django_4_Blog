"""Модели приложения Account."""
from django.contrib.auth import get_user_model
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


class Contact(models.Model):
    user_from = models.ForeignKey('auth.User',
                                  related_name='rel_from_set',
                                  on_delete=models.CASCADE)
    user_to = models.ForeignKey('auth.User',
                                related_name='rel_to_set',
                                on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']

    def __str__(self):
        return f'{self.user_from} подписался на {self.user_to}'


user_model = get_user_model()
user_model.add_to_class('following',
                        models.ManyToManyField('self',
                                               through=Contact,
                                               related_name='followers',
                                               symmetrical=False)
                        )
