"""Настройка админки в приложении Images."""

from django.contrib import admin

from .models import Image


@admin.register(Image)
class Image(admin.ModelAdmin):
    """Настройка админ-панели для модели Image."""

    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['title']

