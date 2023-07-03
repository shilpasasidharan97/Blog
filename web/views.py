from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'web/home.html')


def login_view(request):
    return render(request, 'web/login.html')

def register_view(request):
    return render(request, 'web/register.html')