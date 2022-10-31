from django.urls import path
from .views import RegisterView,SignInAPI

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login',SignInAPI.as_view()),

  
]