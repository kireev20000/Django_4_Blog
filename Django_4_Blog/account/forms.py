"""Формы для блока авторизации."""

from django import forms
from django.contrib.auth.models import User

from .models import Profile


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
        """Функция проверки, что пароли совпадают."""
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают!')
        return cd['password2']

    def clean_email(self):
        """Функция проверки уникальности email."""
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Такой Email уже занят!')
        return data


class UserEditForm(forms.ModelForm):
    """Форма редактирования аккаунта."""

    class Meta:
        """Класс мета формы редактирования аккаунта."""

        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        """Функция проверки уникальности email."""
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id) \
            .filter(email=data)
        if qs.exists():
            raise forms.ValidationError('Такой email уже занят!')
        return data


class ProfileEditForm(forms.ModelForm):
    """Форма редактирования профиля."""

    class Meta:
        """Класс мета формы редактирования профиля."""

        model = Profile
        fields = ['date_of_birth', 'photo']
