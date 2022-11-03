import pytest
from rest_framework.test import APIClient
from users.serializers import UserSerializer
from unittest import TestCase
from users.models import CustomUser
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.test import force_authenticate
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory

@pytest.fixture
def auth_client(db): 
   
    client = APIClient()
    def get_auth_client(cur_user = None):
       
        if (cur_user is None):
            user=CustomUser.objects.create_user(username="hoss",password="123456")
            user.save()
            cur_user=authenticate(username="hoss",password="123456")
      
            response=client.post('/api/login',{'username':"hoss",'password':"123456"},format="json")
            data=response.data
            token=data['token']
            client.credentials(HTTP_AUTHORIZATION='Token' + token)
            client.force_authenticate(user=cur_user)
        
        else :
            client.force_authenticate(user=cur_user)
        
        return client
    
    return get_auth_client