from django.contrib import admin
from .models import Profile

# Register your models here.
# Отображение таблиы профиля в админ панеле
admin.site.register(Profile)