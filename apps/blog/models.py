from django.db import models
from datetime import datetime

# Создан класс модель для блогов/публикаций
class Publication(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=15)
    short_description = models.CharField(max_length=30, blank=True)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    text = models.TextField("Текст")

    class Meta:
        ordering = ['author', '-pub_date', ]

    def __str__(self):
        return self.title

# Создан класс модель со связью один к одному для комментариев к блогам/публикациям
class Comments(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    new = models.ForeignKey(Publication, on_delete=models.CASCADE)
    text = models.TextField("Комментарий")
    created = models.DateTimeField(auto_now_add=True, null=True)
    moderation = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.user)