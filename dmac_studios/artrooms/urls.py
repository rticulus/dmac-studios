from django.urls import path, include
from. import views

urlpatterns = [
    path('home', views.home, name='art-home'),
]


urlpatterns = [
    path('gallery', views.home, name='art-gallery'),
]