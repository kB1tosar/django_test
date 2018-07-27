from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="accounts"
urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('registration/', views.registration_user, name='registration'),
    path('registration_next/', views.profile, name='registration_next'),
    path('personalcab/', views.personal_cabinet, name='personalcab'),
    path('user_publication/', views.user_publication, name='user_publication'),
    path('edit_profile/<int:pk>', views.edit_profile, name='edit_profile')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
