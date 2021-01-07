from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='shop-home'),
    path('accounts/', include('allauth.urls')),
]
