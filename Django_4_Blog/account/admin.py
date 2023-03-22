"""Настройка админки в приложении Account."""

from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Админка профилей пользователей."""

    list_display = ['user', 'date_of_birth', 'photo']
    raw_id_fields = ['user',]
