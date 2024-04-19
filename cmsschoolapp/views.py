from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login as auth_login , logout as auth_logout
from django.contrib.auth.models import User

# Create your views here.
def dashboard(request):
    return render(request , "dashboard.html")
def signup(request):
    return render(request , "signup.html")

def signin(request):
    return render(request , "signin.html")