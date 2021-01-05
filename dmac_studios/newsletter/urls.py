from django.urls import path, include
from. import views

urlpatterns = [
    path('blog', views.blog, name='newsletter-blog'),
    path('directorsblog', views.directorsblog, name='newsletter-directorsblog'),
    path('accounts/', include('allauth.urls')),
]