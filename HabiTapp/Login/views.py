from django.shortcuts import render, redirect


# Create your views here.

def HomePage(request):
    return render(request, 'Home Page.html')
