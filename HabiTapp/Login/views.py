import re
from urllib import request
from django.shortcuts import render, redirect


# Create your views here.

def HomePage(request):
    return render(request, 'Home Page.html')

def LoginPage(request):
    return render(request, 'Login Page.html')

def Dashboard(request):
    return render(request, 'Dashboard/Dashboard.html')
    
