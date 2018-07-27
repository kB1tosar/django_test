from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .forms import UserRegistrationForm, ProfileForm
from django.contrib.auth.models import User
from .models import Profile
from blog.views import publication
from django.contrib.auth.decorators import login_required

# Create your views here.

# Создана функция для отображения формы регистрации на html странице
def registration_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # password_second = form.cleaned_data['password_second']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username,
                                            email=email,
                                            password=password,
                                            # password_second = password_second
                                            )
            messages.success(request, 'Спасибо за регистрацию!'.format(user.username))
            return HttpResponseRedirect(reverse('accounts:login'))
    else:
        form = UserRegistrationForm()
    context = {'form':form}
    return render(request, 'accounts/registration.html', context)

# Создана функция для отображения формы входа для пользователя на html странице
def login_user(request):
    if request.method == "POST":
        email = request.POST.get('username')
        password = request.POST.get('password_login')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('accounts:personalcab'))
        else:
            messages.error(request, 'Неверный логин или пароль')

    return render(request, 'accounts/login.html', {})

# Создана функция для отображения формы выхода для пользователя из сайта
def logout_user(request):
    logout(request)
    return HttpResponseRedirect (reverse('homepage:index'))

# Создана функция для отображения формы для измения профиля пользователя на html странице
@login_required
def edit_profile(request, pk):
    edit_profile1 = get_object_or_404(Profile, pk=pk)
    not_this_user = get_object_or_404(Profile, id=pk)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=edit_profile1)
        if form.is_valid():
            edit_profile = form.save(commit=False)
            edit_profile.user = request.user
            edit_profile.save()
            return redirect('accounts:personalcab')
    else:
        form = ProfileForm(instance=edit_profile1)
    context = {'form': form, 'not_this_user': not_this_user, }
    return render(request, 'accounts/edit_profile.html', context)

# Создана функция для отображения формы для создания профиля пользователя на html странице
@login_required
def profile(request):
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            new_profile = profile_form.save(commit=False)
            new_profile.save()
            return HttpResponseRedirect(reverse('accounts:personalcab'))
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    context = {'profile_form': profile_form}
    return render(request, 'accounts/registration_next.html', context)

# Создана функция для отображения личного кабинета пользователя на html странице
@login_required
def personal_cabinet(request):
    return render(request, 'accounts/personal_cabinet.html')

# Создана функция для отображения блогов/публикаций пользователя на html странице в личном кабинете
@login_required
def user_publication(request):
    user_pub = publication.objects.all()
    context = {'user_pub': user_pub}
    return render(request, 'accounts/user_publication.html', context)
