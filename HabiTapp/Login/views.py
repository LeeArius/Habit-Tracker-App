import re
from urllib import request
from django.shortcuts import render, redirect


# Create your views here.

def HomePage(request):
    return render(request, 'Home Page.html')

def LoginPage(request):
    return render(request, 'Login Page.html')

def SignUp(request):
    return render(request, 'SignUp Page.html')

def Dashboard(request):
    return render(request, 'Dashboard/Dashboard.html')

def WD(request):
    return render(request, 'Dashboard/Wind Down.html')

def WD2(request):
    return render(request, 'Dashboard/Wind Down2.html')

def FM(request):
    return render(request, 'Dashboard/Focus Mode.html')

def FM2(request):
    return render(request, 'Dashboard/Focus Mode2.html')
    
def MUA(request):
    return render(request, 'Dashboard/MUA.html')
