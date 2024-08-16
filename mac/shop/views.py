from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

# Create your views here.

def index(request):

    return render(request, 'shop/index.html')

def about(request):

    return render(request, 'shop/about.html')

def contact(request):

    return render(request, 'shop/contact.html')

def tracker(request):

    return render(request, 'shop/tracker.html')

def productview(request):

    return render(request, 'shop/productview.html')

def checkout(request):

    return render(request, 'shop/checkout.html')

def search(request):

    return render(request, 'shop/search.html')
