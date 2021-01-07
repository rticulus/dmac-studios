from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='newsletter-home'),
    path('director/', views.director, name='newsletter-director'),
    path('accounts/', include('allauth.urls')),
]
