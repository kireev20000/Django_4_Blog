"""Формы для картинок."""

from django import forms

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

    def clean_url(self):
        """Проверка что картинка имеет нужный формат."""
        url = self.cleaned_data['url']
        valid_extensions = ['jpeg', 'jpg', 'png']
        extension = url.rsplit(',', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('Формат картинки может быть'
                                        ' только jpeg, jpg или png.')
        return url