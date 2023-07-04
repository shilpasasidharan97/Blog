from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.


def home(request):
    return render(request, 'web/home.html')


def login_view(request):
    return render(request, 'web/login.html')

def logout_view(request):
    logout(request)
    return redirect('web:login_view')


def register_view(request):
    return render(request, 'web/register.html')