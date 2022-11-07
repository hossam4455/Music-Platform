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


@pytest.mark.django_db
def test_album_create_endpoint_post(auth_client):
    user = CustomUser.objects.create(
        username="hossam", email="h@h.com", password1="123456", password2="123456",)

    artists = Artists.objects.create(
        Artist_name="asdas", Artist_link="h@h.com", user=user)

    response = auth_client().post('/albums/create/',
     {'Artist_name': "asdas", 'Album_name': "alial", 'Cost': "22.0", 'Is_approved': "True", 'Release_datetime': "2022-7-6"}, format="json")
    
    assert  response.status_code == 200
    print(Album.objects.all())
