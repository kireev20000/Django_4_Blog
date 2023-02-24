"""Настройка приложения Post."""
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """Класс настройки приложения Blog."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
