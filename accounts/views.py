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

@login_required
def edit_profile(request, pk):
    edit_profile1 = get_object_or_404(Profile, pk=pk)
    not_this_user = get_object_or_404(Profile, id=pk)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=edit_profile1)
        if form.is_valid():
            edit_profile = form.save(commit=False)
            edit_profile.user = request.user
            edit_profile.save()
            return redirect('accounts:personalcab')
    else:
        form = ProfileForm(instance=edit_profile1)
    return render(request, 'accounts/edit_profile.html', {'form': form, 'not_this_user': not_this_user})

@login_required
def profile(request):
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            new_profile = profile_form.save(commit=False)
            new_profile.save()
            # messages.success(request, 'Спасибо за регистрацию!')
                             # .format(user.username))
            return HttpResponseRedirect(reverse('accounts:persobalcab'))
    else:
        profile_form = ProfileForm()
    return render(request, 'accounts/registration_next.html', {'profile_form': profile_form})

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

def logout_user(request):
    logout(request)
    return HttpResponseRedirect (reverse('homepage:index'))

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
            return HttpResponseRedirect(reverse('accounts:login'))
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/registration.html',{'form':form})

@login_required
def personal_cabinet(request):
    return render(request, 'accounts/personal_cabinet.html')

@login_required
def user_publication(request):
    user_pub = publication.objects.all()
    return render(request, 'accounts/user_publication.html', {'user_pub': user_pub})



# @login_required
# @transaction.atomic
# def profile(request):
#     if request.method == 'POST':
#         User_form = UserForm(request.POST, instance=request.user)
#         Profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if User_form.is_valid() and Profile_form. is_valid():
#             User_form.save()
#             Profile_form.save()
#             return HttpResponseRedirect('you are now registered')
#     else:
#         User_form = UserForm(instance=request.user)
#         Profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'accounts/personal_cabinet.html', {
#         'User_form': User_form,
#         'Profile_form': Profile_form
#
#         })

# def additional(request):
#     if request.method == 'POST':
#         form_additional = additional_data(request.POST)
#         if form_additional.is_valid():
#             # form_additional = form_additional.save(commit=False)
#             # form_additional.save()
#             first_name = form_additional.cleaned_data['first_name']
#             last_name = form_additional.cleaned_data['last_name']
#             user = User.objects.create_user(first_name=first_name, last_name=last_name)
#             # return HttpResponseRedirect(reverse('accounts:registration_next'))
#     else:
#         form_additional = additional_data()
#     return render(request, 'accounts/registration_next.html', {'form_additional':form_additional} )

