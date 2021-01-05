from django.urls import path, include
from. import views

urlpatterns = [
    path('home', views.home, name='bookings-home'),
    path('aboutus/', views.aboutus, name='bookings-about'),
    path('accounts/', include('allauth.urls')),
]