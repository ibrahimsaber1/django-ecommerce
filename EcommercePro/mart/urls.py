from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mart/', views.mart, name='mart'),
    path('cart/', views.cart, name='cart'),
]