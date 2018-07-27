# Generated by Django 2.0.2 on 2018-07-22 15:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180721_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='publication',
            name='short_description',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='publication',
            name='title',
            field=models.CharField(max_length=15),
        ),
    ]
