"""Вью-сет приложения Account."""


from django.shortcuts import render
# from django.contrib.auth import authenticate, login
# from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, \
                   UserEditForm, ProfileEditForm
from .models import Profile


@login_required
def dashboard(request):
    """Вью вывода дашборда."""
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

# def user_login(request):
#     """Функция логина пользователя."""
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request,
#                                 username=cd['username'],
#                                 password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Аутентификация прошла успешно!')
#                 else:
#                     return HttpResponse('Ваш аккаунт неактивен!')
#             else:
#                 HttpResponse('Неверный логин или пароль!')
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form': form})


def register(request):
    """Вью регистрации нового пользователя."""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})


@login_required
def edit(request):
    """Вью редактирования профиля."""
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Профиль успешно обновлен!')
        else:
            messages.error(request, 'Ошибка при обновлении профиля!')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
            instance=request.user.profile)
    return render(request, 'account/edit.html',
                  {'user_form': user_form, 'profile_form': profile_form})
