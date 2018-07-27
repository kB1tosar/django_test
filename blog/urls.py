from django.urls import path
from . import views

app_name="blog"
urlpatterns = [
    path('create_blogs/', views.blog_new, name='create_blog'),
    path('edit_blog/', views.blog_edit, name='edit_blog'),
    path('blog_view/', views.blog_list, name='blog_view'),
    path('blog_view/<int:pk>', views.blog_list, name='blog_view'),
    path('full_blog/<int:pk>', views.blog_detail, name='full_blog'),
    path('blog_remove/<int:pk>', views.blog_remove, name='blog_remove'),
    path('blog_edit/<int:pk>', views.blog_edit, name='blog_edit'),
]
