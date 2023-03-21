"""Формы для блока авторизации."""

from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """Формы ввода логина и пароля."""

    username = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')


class UserRegistrationForm(forms.ModelForm):
    """Форма создания нового пользователя."""

    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль:',
                                widget=forms.PasswordInput)

    class Meta:
        """Класс мета для формы регистрации пользователя."""

        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают!')
        return cd['password2']
