from django.urls import path

from . import views

urlpatterns = [
 
    path('create/', views.AlbumCreat.as_view(), name='new_album'),
    path('', views.AlbumList.as_view(), name='Albumlist'),
    path('manule/', views.AlbumListManule.as_view(), name='Manule'),
  
    
]