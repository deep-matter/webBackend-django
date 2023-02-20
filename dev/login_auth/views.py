from django.shortcuts import render, redirect
from django.contrib.auth.models import User# Create your views herei.:


def login(request):

    return render(request, "account/login.html")


def signUp(request):
    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    password = request.POST['password']
    password2 = request.POST['password2']
    if password == password2:
        if User.objects.filter(username=username).exists():
            return raise Exception("username already exists")
        else:
             if User.objects.filter(username=username).exists():
                 return raise Exception("email already exists")
             else:
                User.objects.create_user(username=username,first_mame ).


             


    return render(request, "account/signUp.html")


def logout(request):
    return redirect("index")


def dashboard(request):
    return render(request, "account/dashboard.html")
