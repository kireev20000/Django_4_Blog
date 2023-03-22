"""Кастомный бэкэнд для аутентификации пользователей."""

from django.contrib.auth.models import User


class EmailAuthBackend:
    """Аунтификация использую email юзера."""

    def authenticate(self, request, username=None, password=None):
        """Вход по email вместо логина."""
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

    def get_user(self, user_id):
        """Возвращает объект юзера для входа."""
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
