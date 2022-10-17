from django.urls import path

from . import views

urlpatterns = [
 
    path('create/', views.new_album, name='new_album')
]