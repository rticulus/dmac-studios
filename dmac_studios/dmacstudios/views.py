from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'dmacstudios/home.html')


def aboutus(request): 
    return render(request, 'dmacstudios/aboutus.html')


def classes(request): 
    return render(request, 'dmacstudios/classes.html')


def gallery(request): 
    return render(request, 'dmacstudios/gallery.html')