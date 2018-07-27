from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile

# Создана форма для регистрации
class UserRegistrationForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль',
                               max_length=20,
                               min_length=5,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # password_second = forms.CharField(label='Потверждение пароля',
    #                                   max_length=20,
    #                                   min_length=5,
    #                                   widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Ваш логин',
                               max_length=20,
                               min_length=5,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise ValidationError('Пользователь с таким email уже существует!')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise ValidationError('Пользователь с таким логином уже существует!')
        return username

    # def clean_password(self):
    #     cleaned_data = super().clean()
    #     pass1 = cleaned_data.get('password')
    #     pass2 = cleaned_data.get('password_second')
    #
    #     if pass1 and pass2:
    #         if pass1 != pass2:
    #             raise ValidationError('Пароли не совпадают!')

# Создана форма для запонения профиля дополнительными данными
class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя',
                                max_length=20,
                                min_length=2,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия',
                                max_length=20,
                                min_length=1,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    skype = forms.CharField(label='Skype',
                            max_length=20,
                            min_length=2,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Телефон',
                            max_length=20,
                            min_length=2,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    avatar = forms.ImageField(label='Аватар',
                             widget=forms.ClearableFileInput(attrs={'class': 'form-control '})
                             )
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'avatar', 'phone', 'skype')


