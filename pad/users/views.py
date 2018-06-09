from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth

from .forms import LoginForm, RegisterForm

# Dicas
# Para autenticar: user = auth.authenticate(request, username='username', password='password')
# Para logar: auth.login(request, user)
def login(request):
    ctx = {
        'form': LoginForm(),
    }
    
    return render(request, 'users/login.html', ctx)


def register(request):
    ctx = {
        'form': RegisterForm(),
    }
    return render(request, 'users/login.html', ctx)
