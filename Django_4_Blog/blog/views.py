"""Вью-сет приложения Post."""
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import ListView

from .models import Post
from .forms import EmailPostForm, CommentForm


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
    comments = post.comments.filter(active=True)
    form = CommentForm
    return render(request, 'blog/post/detail.html', {'post': post,
                                                     'comments': comments,
                                                     'form': form})


def post_share(request, post_id):
    """Функция отправки поста по Email."""
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} рекомендует вам почитать {post.title}"
            message = f"Прочитай '{post.title}' по ссылке {post_url}\n\n" \
                      f"{cd['name']} добавил комментарий: {cd['comments']}"
            send_mail(subject, message, 'moe_milo@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})


@require_POST  # позволяет только метод пост для этого вью
def post_comment(request, post_id):
    """Функция обработки комментариев."""
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request, 'blog/post/comments.html', {'post': post,
                                                       'form': form,
                                                       'comment': comment})


