"""users_auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from users_app import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls, name='admin_site'),
    url(r'^users_app/', include('users_app.urls')),
    url(r'^lougout/$', views.user_logout, name='user_logout'),
    url(r'^spesial/', views.special, name='special')
]
