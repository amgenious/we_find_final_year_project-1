from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import PasswordsChangeView
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('register', views.register, name = 'register'),

    path('password/', PasswordsChangeView.as_view(template_name = 'change_password.html') , name='change_password'),
    path('password_success',views.password_success, name='password_success'),

    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
