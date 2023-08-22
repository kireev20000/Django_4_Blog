"""Формы для картинок."""

from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify

import requests

from .models import Image


class ImageCreateForm(forms.Form):
    """Форма добавления новой картинки."""

    class Meta:
        """Класс мета формы добавления картинки."""
        model = Image
        fields = ['name', 'url', 'description']
        widgets = {
            'url': forms.HiddenInput,
        }

    def save(self, force_insert=False,
                   force_update=False,
                   commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data('url')
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'
        response = requests.get(image_url)
        image.image.save(image_name,
                         ContentFile(response.content),
                         save=False)
        if commit:
            image.save()

        return image

    def clean_url(self):
        """Проверка, что картинка имеет нужный формат."""
        url = self.cleaned_data['url']
        valid_extensions = ['jpeg', 'jpg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('Формат картинки может быть'
                                        ' только jpeg, jpg или png.')
        return url
