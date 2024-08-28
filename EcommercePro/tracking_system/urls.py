from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_order/', views.add_order, name='add_order'),
    path('postdata/', views.postdata, name='postdata'),  # Map the URL to the postdata view
    
]
