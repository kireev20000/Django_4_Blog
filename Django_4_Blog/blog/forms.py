"""Формы блога."""

from django import forms


class EmailPostForm(forms.Form):
    """Форма отправки поста по Email."""

    name = forms.CharField(max_length=25, label='Заголовок')
    email = forms.EmailField(label='Отправитель:')
    to = forms.EmailField(label='Получатель:')
    comments = forms.CharField(required=False, widget=forms.Textarea)
