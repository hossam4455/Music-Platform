import email
from http import client
from urllib import response
import pytest
from rest_framework.test import APIClient
from unittest import TestCase
from conftest import auth_client
from users.models import CustomUser
from rest_framework.test import RequestsClient
from artists.models import Artists

class TestArtist():
    @pytest.mark.django_db
    def test_artist_create(dp):
        
       Artists.objects.create(Artist_name="hossam",Artist_link="https://www.linkedin.com/feed/")
       assert Artists.objects.count()==1
