"""Кастомные темплейт тэги для шаблонов."""
from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe

import markdown

from ..models import Post


register = template.Library()


@register.simple_tag  # кастомное имя simple_tag(name='мой_tag')
def total_posts():
    """Кастомный тэмплейт-тэг для шаблона, возвр. кол-во опуб. постов."""
    return Post.published.all().count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    """Вовращает рендер вложенной страницы в тэг, 5 послед. постов"""
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_post': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')
                                   ).order_by('-total_comments')[:count]

@register.filter(name='markdown')
def markdown_format(text):
    """Конвертирует текст Markdown в HTML."""
    return mark_safe(markdown.markdown(text))
