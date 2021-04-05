"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from users.views import CustomLoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("website.urls")),
    path('kayit', user_views.register, name='register'),
    path('giris', CustomLoginView.as_view(
        template_name='users/login.html'), name='login'),
    path('cikis', auth_views.LogoutView.as_view(
        template_name='users/logout.html'), name='logout'),
    path('profil/', user_views.profile, name='profile'),
    path('sifremi-unuttum/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='forgot-password'),
    path('sifremi-unuttum/basarili/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('sifre-sifirla/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('sifre-degistirildi/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('hesabi-sil/', user_views.delete_user, name='delete_account'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)