from django.urls import path

from . import views

urlpatterns = [
 
    path('create/', views.new_album.as_view(), name='new_album')
]