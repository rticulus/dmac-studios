from django.urls import path, include
from. import views

urlpatterns = [
    path('', views.home, name='dmacstudios-home'),
    path('aboutus/', views.aboutus, name='dmacstudios-aboutus'),
    path('classes/', views.classes, name='dmacstudios-classes'),
    path('gallery/', views.gallery, name='dmacstudios-gallery'),
    path('accounts/', include('allauth.urls')),
]