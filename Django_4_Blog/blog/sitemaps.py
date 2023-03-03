"""Карта сайта для Блога."""
from django.contrib.sitemaps import Sitemap

from .views import Post


class PostSitemap(Sitemap):
    """Карта сайта."""

    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        """Возвращает квари-сет для построение карты сайта."""
        return Post.published.all()

    def lastmod(self, obj):
        """Получает ретёрн items и возвращает дату изменения."""
        return obj.updated
