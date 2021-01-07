from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='dmacstudios-home'),
    path('about/', views.about, name='dmacstudios-about'),
    path('accounts/', include('allauth.urls')),
]
