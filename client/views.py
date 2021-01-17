from django.shortcuts import render, redirect
from django .contrib import messages
from .forms import UserRegisterForm


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'DMAC account created for {username}, You must now login to continue')
            return redirect('dmacstudios-home')
    else:
        form = UserRegisterForm()
    return render(request, 'client/signup.html', {'form': form})


def login(request):
    form = UserRegisterForm()
    return render(request, 'client/login.html', {'form': form})
