from django.contrib import admin
from .models import Publication, Comments
# Register your models here.

admin.site.register(Publication)

class CommentAdmin(admin.ModelAdmin):
    """ Комментарии
    """
    list_display = ('user', 'new', 'created', 'moderation')


admin.site.register(Comments, CommentAdmin)