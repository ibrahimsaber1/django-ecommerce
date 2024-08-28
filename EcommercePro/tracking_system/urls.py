from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('postdata/', views.postdata, name='postdata'),  # Map the URL to the postdata view
    
]
