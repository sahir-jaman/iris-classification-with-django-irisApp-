from . import views
from django.urls import path

urlpatterns = [
    path('', views.Welcome, name='Welcome'),
    path('user', views.User, name= 'User'),
]
