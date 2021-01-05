from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('<h1>DMACStudios Home</h1>')

def aboutus(request):
    return HttpResponse('<h1>DMACStudios About Us</h1>')
