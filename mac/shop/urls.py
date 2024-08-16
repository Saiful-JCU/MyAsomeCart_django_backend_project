
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
            path('', views.index, name="ShopHome"),
            path('about/', views.about, name="aAboutUS"),
            path('contact/', views.contact, name="ContactUS"),
            path('tracker', views.tracker, name="TrakingOrder"),
            path('search', views.search, name="Search"),
            path('productview', views.productview, name="ProductView"),
            path('checkout', views.checkout, name="CheckOut"),
        ]