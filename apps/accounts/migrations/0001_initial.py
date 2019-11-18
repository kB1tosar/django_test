# Generated by Django 2.0.2 on 2018-07-27 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=20)),
                ('last_name', models.CharField(blank=True, max_length=20)),
                ('skype', models.CharField(blank=True, max_length=15)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('avatar', models.ImageField(blank=True, upload_to='accounts/templates/Image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]