from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .views import views_main, views_users

# app_name = 'thebreeze_app'

urlpatterns = [
    
    path('', views_main.homepage, name='homepage'),

    # User related
    path('user/profile/<int:user_pk>/', views_users.user_profile, name='user_profile'),
    path('user/profile/edit/<int:user_pk>/', views_users.edit_user, name='edit_user'),
    path('user/profile/me/', views_users.my_user_profile, name='my_user_profile'),
    path('goodbye/', views_users.goodbye, name="goodbye"),
    # Account related
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', views_users.register, name='register'),

]