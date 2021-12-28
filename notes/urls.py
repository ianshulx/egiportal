
from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
   
    path('notes/', views.notes, name='notes'),
    path('bca/', views.bca, name='bca'),
    path('btech/', views.btech, name='btech'),


    path('bca_sem1/', views.bca_sem1, name='bca_sem1'),
    path('bca_sem2/', views.bca_sem2, name='bca_sem2'),
    path('bca_sem3/', views.bca_sem3, name='bca_sem3'),
    path('bca_sem4/', views.bca_sem4, name='bca_sem4'),
    path('bca_sem5/', views.bca_sem5, name='bca_sem5'),
    path('bca_sem6/', views.bca_sem6, name='bca_sem6'),
    


    path('btech_first/', views.btech_first, name='btech_first'),
    path('btech_first_sem1/', views.btech_first_sem1, name='btech_first_sem1'),
    path('btech_first_sem2/', views.btech_first_sem2, name='btech_first_sem2'),



    path('btech_cs/', views.btech_cs, name='btech_cs'),
    path('btech_cs_sem1/', views.btech_cs_sem1, name='btech_cs_sem1'),
    path('btech_cs_sem2/', views.btech_cs_sem2, name='btech_cs_sem2'),
    path('btech_cs_sem3/', views.btech_cs_sem3, name='btech_cs_sem3'),
    path('btech_cs_sem4/', views.btech_cs_sem4, name='btech_cs_sem4'),
    path('btech_cs_sem5/', views.btech_cs_sem5, name='btech_cs_sem5'),
    path('btech_cs_sem6/', views.btech_cs_sem6, name='btech_cs_sem6'),



    path('btech_ce/', views.btech_ce, name='btech_ce'),
    path('btech_ce_sem1/', views.btech_ce_sem1, name='btech_ce_sem1'),
    path('btech_ce_sem2/', views.btech_ce_sem2, name='btech_ce_sem2'),
    path('btech_ce_sem3/', views.btech_ce_sem3, name='btech_ce_sem3'),
    path('btech_ce_sem4/', views.btech_ce_sem4, name='btech_ce_sem4'),
    path('btech_ce_sem5/', views.btech_ce_sem5, name='btech_ce_sem5'),
    path('btech_ce_sem6/', views.btech_ce_sem6, name='btech_ce_sem6'),



    path('btech_ec/', views.btech_ec, name='btech_ec'),
    path('btech_ec_sem1/', views.btech_ec_sem1, name='btech_ec_sem1'),
    path('btech_ec_sem2/', views.btech_ec_sem2, name='btech_ec_sem2'),
    path('btech_ec_sem3/', views.btech_ec_sem3, name='btech_ec_sem3'),
    path('btech_ec_sem4/', views.btech_ec_sem4, name='btech_ec_sem4'),
    path('btech_ec_sem5/', views.btech_ec_sem5, name='btech_ec_sem5'),
    path('btech_ec_sem6/', views.btech_ec_sem6, name='btech_ec_sem6'),




    path('btech_me/', views.btech_me, name='btech_me'),
    path('btech_me_sem1/', views.btech_me_sem1, name='btech_me_sem1'),
    path('btech_me_sem2/', views.btech_me_sem2, name='btech_me_sem2'),
    path('btech_me_sem3/', views.btech_me_sem3, name='btech_me_sem3'),
    path('btech_me_sem4/', views.btech_me_sem4, name='btech_me_sem4'),
    path('btech_me_sem5/', views.btech_me_sem5, name='btech_me_sem5'),
    path('btech_me_sem6/', views.btech_me_sem6, name='btech_me_sem6'),



    path('btech_ee/', views.btech_ee, name='btech_ee'),
    path('btech_ee_sem1/', views.btech_ee_sem1, name='btech_ee_sem1'),
    path('btech_ee_sem2/', views.btech_ee_sem2, name='btech_ee_sem2'),
    path('btech_ee_sem3/', views.btech_ee_sem3, name='btech_ee_sem3'),
    path('btech_ee_sem4/', views.btech_ee_sem4, name='btech_ee_sem4'),
    path('btech_ee_sem5/', views.btech_ee_sem5, name='btech_ee_sem5'),
    path('btech_ee_sem6/', views.btech_ee_sem6, name='btech_ee_sem6'),


    path('bca_sem', views.bca_sem, name='bca_sem'),
    path('bca_sem1', views.bca_sem1, name='bca_sem1'),
    path('bca_sem2', views.bca_sem2, name='bca_sem2'),
    path('bca_sem3', views.bca_sem3, name='bca_sem3'),
    path('bca_sem4', views.bca_sem4, name='bca_sem4'),
    path('bca_sem5', views.bca_sem5, name='bca_sem5'),
    path('bca_sem6', views.bca_sem6, name='bca_sem6'),




]
