from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request,'robotAnfibio/inicio.html')

def login(request):
    return render(request,'robotAnfibio/login.html')