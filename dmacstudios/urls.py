from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dmacstudios-home'),
    path('about/', views.about, name='dmacstudios-about'),
]
