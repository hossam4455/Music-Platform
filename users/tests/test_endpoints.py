import email
from http import client
from urllib import response
import pytest
from rest_framework.test import APIClient
from unittest import TestCase
from conftest import auth_client
from users.models import CustomUser
from rest_framework.test import RequestsClient


class TestUser():

    client = APIClient()

    @pytest.mark.django_db
    def test_get_authenticated_get_fail(self):
        response = self.client.get('/users/1/')
        assert response.status_code == 403

    def test_get_authenticated_put_fail(self):
        response = self.client.put('/users/1/')
        assert response.status_code == 403

    def test_get_authenticated_patch_fail(self):
        response = self.client.patch('/users/1/')
        assert response.status_code == 403

    @pytest.mark.django_db
    def test_get_authenticated_get(self, auth_client):

        response = auth_client().get('/users/1/')
        assert response.status_code == 200
        print(response.data)

    def test_get_authenticate_put(self, auth_client):

        response = auth_client().put('/users/1/',
                                     {'username': "hossam", 'password1': "123456", 'password2': "123456", 'email': "h@h.com"}, format="json")

        assert response.data['username'] == "hossam" and response.data['email'] == "h@h.com" and response.status_code == 200

        print(response.data)

    def test_get_authenticate_patch(self, auth_client):

        response = auth_client().patch(
            '/users/1/', {'username': "hossam1", 'password': "123456"}, format="json")
        assert response.data['username'] == "hossam1" and response.data['email'] == "" and response.status_code == 200
        print(response.data)
