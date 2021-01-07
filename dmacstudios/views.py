from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>This is my DMAC Studios Home Page</h1>')


def about(request):
    return HttpResponse('<h1>DMAC Studios About Page</h1>')
