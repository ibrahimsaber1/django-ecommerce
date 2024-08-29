from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.product , name='product'),
    path('/products', views.products , name='products')

]
