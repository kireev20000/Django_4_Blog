"""RSS-фид для Блога."""

import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from .models import Post


class LatestPostsFeed(Feed):
    """RSS-канал сайта."""

    title = 'Мой блог на Джанге 4'
    link = reverse_lazy('blog:post_list')
    description = 'Новые посты в Блоге на Джанге 4!'

    def items(self):
        """Возвращает квари-сет для построения RSS."""
        return Post.published.all()[:5]

    def item_title(self, item):
        """Возвращает имя поста."""
        return item.title

    def item_description(self, item):
        """Возвращает краткое описание поста."""
        return truncatewords_html(markdown.markdown(item.body), 30)

    def item_pubdate(self, item):
        """Возвращает дату публикации поста."""
        return item.publish
