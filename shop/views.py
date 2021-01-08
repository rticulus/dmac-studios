from django.shortcuts import render


def index(request):
    return render(request, 'shop/index.html')



def home(request):
    return render(request, 'shop/home.html')
