"""egi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views


urlpatterns = [
    
    path('', include('authentication.urls')),
    # path('', include('home.urls')),
    # path('', include('home.urls')),
    
    path('frequently/', views.frequently, name='frequently'),
    path('hod/', views.hod, name='HOD'),
    path('sources/', views.sources, name='sources'),
    path('team/', views.team, name='team'),
    path('notice/', views.notice, name='notice'),
    path('event/', views.event, name='event'),
    path('quiz/', views.quize, name='quiz'),
    path('library/', views.library, name='library'),
    path('gallary/', views.gallary, name='gallary'),
    path('not/', views.not_available, name='not'),
    path('not2/', views.not_available2, name='not2'),

    

   
    
    

]
