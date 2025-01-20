from django.urls import path, include
from django import views
from .views import *


urlpatterns = [
    path('',home, name='home'),
    path('login/',login, name='login'),
    path('register/',register, name='register'),
    path('gallery/',gallery, name='gallery'),
    path('<int:myid>',detail, name='detail'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
    path('gestionProjet/',gestionProjet, name='gestionProjet'),
    path('andmtm/',andmtm, name='andmtm'),
]
