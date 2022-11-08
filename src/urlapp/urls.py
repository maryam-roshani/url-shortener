from django.urls import path
from .import views


app_name = 'urlapp' 

urlpatterns = [
    path('', views.home, name='home'),
]