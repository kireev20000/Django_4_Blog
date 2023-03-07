"""Настройка приложения Account."""
from django.apps import AppConfig


class AccountConfig(AppConfig):
    """Класс настройки приложения Account."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'
