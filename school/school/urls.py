"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from studentinfo import views
from register import views as v

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', v.register, name='register'),
    path('login/',v.user_login, name='user_login'),
    path('logout/',v.user_logout, name='user_logout'),
    path('',views.IndexView.as_view(), name="index"),
    path('student_info/', include('studentinfo.urls', namespace='studentinfo')),
    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='change_password'),
    path('change-password/done/',auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
