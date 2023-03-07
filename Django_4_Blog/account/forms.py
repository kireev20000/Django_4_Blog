"""Формы для блока авторизации."""

from django import forms


class LoginForm(forms.Form):
    """Формы ввода логина и пароля."""
    username = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
