"""teacher_feedback_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views
from user import views as user_views
from feedback import views as feedback_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_views.login, name='login'),
    path('home/',user_views.home ,name='home'),
    path('home_teacher/',user_views.home_teacher ,name='home_teacher'),
    path('feedback_form/',feedback_views.feedback_form ,name='feedback_form'),
    path('feedback/',feedback_views.feedback,name='feedback'),
    path('logout/',user_views.logout_view ,name='logout'),
    path('base/',feedback_views.base,name='base'),
]
