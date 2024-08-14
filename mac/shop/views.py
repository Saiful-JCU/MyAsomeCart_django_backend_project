from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

# Create your views here.

def index(request):

    return render(request, 'shop/index.html')