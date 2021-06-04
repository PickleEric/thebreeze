from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .views import views_main

# app_name = 'thebreeze_app'

urlpatterns = [
    
    path('', views_main.homepage, name='homepage'),

]