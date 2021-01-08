from django.shortcuts import render


def index(request):
    return render(request, 'dmacstudios/index.html')


def home(request):
    return render(request, 'dmacstudios/home.html')


def about(request):
    return render(request, 'dmacstudios/about.html')
