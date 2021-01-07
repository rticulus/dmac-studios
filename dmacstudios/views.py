from django.shortcuts import render


def home(request):
    return render(request, 'dmacstudios/home.html')


def about(request):
    return render(request, 'dmacstudios/about.html')
