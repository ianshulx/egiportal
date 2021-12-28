from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('main', views.main, name='main'),
    path('signup', views.signup, name='signup'),
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('welcome', views.welcome, name='welcome'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
]
  