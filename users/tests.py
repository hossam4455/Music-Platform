from urllib import response
from django.test import TestCase
from rest_framework import status
from rest_framework.test import RequestsClient
# Create your tests here.
class usersdetailtest(TestCase):
  
    def test_get_user_found(self):
        #response=self.client.post('/users/{1}/')
        #factory = APIRequestFactory()
        self.client.post('/api/register',{   "username": "updsadahhhhhhheted11","email": "a@a.com","password1": "12456","password2": "12456"})
        self.client.post('/api/login',{   "username": "updsadahhhhhhheted11","password": "12456"})
        #self.client.get({'/api-auth/logout'})
        response =self.client.get( f'/users/{1}/')
       # self.assertEqual (response.status_code,200)   
        print(response)
        
        