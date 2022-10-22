from re import template
from django.urls import path
from . import views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  views as auth_views
urlpatterns = [
    path('', views.home.as_view() , name='home'),
    path('signup/', views.signup.as_view() , name='signup'),
    path('sigin', auth_views.LoginView.as_view(template_name='login.html'),name='sigin'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    
]