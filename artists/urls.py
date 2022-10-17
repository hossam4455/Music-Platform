from django.urls import path

from . import views
from .views import view_artists
urlpatterns = [
   
    path('create/', views.new_artist, name='new_artist'),

    path('',view_artists, name='new_artist')
]