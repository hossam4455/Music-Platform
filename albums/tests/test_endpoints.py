import email
from http import client
from urllib import response
import pytest
from rest_framework.test import APIClient
from unittest import TestCase
from conftest import auth_client
from users.models import CustomUser
from rest_framework.test import RequestsClient
from albums.models import Album
from artists.models import Artists
from users.models import CustomUser
import urllib.request
from ..serializers_album import AlbumSerializer, AlbumCreateSeriakizer

client = APIClient()

class TestEndPoint():
    
        
    def test_album_create_protection(self,dp):
        user = CustomUser.objects.create(
        username="hossam", email="h@h.com", password1="123456", password2="123456",)

        artists = Artists.objects.create(
            Artist_name="asdas", Artist_link="h@h.com", user=user)
        album = Album.objects.create(Artist_name=artists, Album_name='alial',
                                 Cost='22.0', Is_approved='True', Release_datetime='2022-7-6')
        serilalizer=AlbumCreateSeriakizer(album)
        data=serilalizer.data
        print(Artists.objects.all())
        response = client.post('/albums/create/',serilalizer.data)
    
        assert  response.status_code == 403  
    def test_album_create_endpoint_post(self,auth_client):
        user = CustomUser.objects.create(
            username="hossam", email="h@h.com", password1="123456", password2="123456",)

        artists = Artists.objects.create(
            Artist_name="asdas", Artist_link="h@h.com", user=user)
        album = Album.objects.create(Artist_name=artists, Album_name='alial',
                                 Cost='22.0', Is_approved='True', Release_datetime='2022-7-6')
        serilalizer=AlbumCreateSeriakizer(album)
        data=serilalizer.data
        print(Artists.objects.all())
        response = auth_client().post('/albums/create/',serilalizer.data)
        assert data['Album_name'] == album.Album_name
        assert float(data['Cost']) == float(album.Cost)
        assert bool(data['Is_approved']) == bool(album.Is_approved)
        assert data['Release_datetime'] == album.Release_datetime
    
        assert  response.status_code == 201
    def test_album_cost_must_be_postive_integer(self,auth_client):
        user = CustomUser.objects.create(
        username="hossam", email="h@h.com", password1="123456", password2="123456",)

        artists = Artists.objects.create(
            Artist_name="asdas", Artist_link="h@h.com", user=user)
        album = Album.objects.create(Artist_name=artists, Album_name='alial',
                                 Cost='-22.0', Is_approved='True', Release_datetime='2022-7-6')
        serilalizer=AlbumCreateSeriakizer(album)
        data=serilalizer.data
        print(Artists.objects.all())
        response = auth_client().post('/albums/create/',serilalizer.data)
    
        assert  response.status_code == 400
 
  
