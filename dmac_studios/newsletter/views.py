from django.shortcuts import render

# Create your views here.

def blog(request):
    return render(request, 'newsletter/blog.html')


def directorsblog(request): 
    return render(request, 'newsletter/directorsblog.html')
