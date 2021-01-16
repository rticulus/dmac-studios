from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    form = UserCreationForm()
    return render(request, 'client/signup.html', {'form': form})


def login(request):
    form = UserCreationForm()
    return render(request, 'client/login.html', {'form': form})
