"""Вью-сет приложения Post."""
from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Post


def post_list(request):
    """Возвращает все посты блога на страницу."""
    posts_list = Post.published.all()
    paginator = Paginator(posts_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/list.html',
                  {'page_obj': posts})


class PostListView(ListView):
    """Альтернативный index на CBV."""
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_detail(request, year, month, day, post):
    """Возвращает выбранный пост по ID."""
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
