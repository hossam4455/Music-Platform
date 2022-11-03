from django.shortcuts import render
from lib2to3.pgen2 import token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from users.models import CustomUser
import jwt, datetime
from rest_framework.decorators import api_view
from rest_framework import generics, permissions, serializers
from rest_framework import generics
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from rest_framework.authentication import BasicAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view, permission_classes
from knox.auth import TokenAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from rest_framework import status
from django.contrib.auth.signals import user_logged_in, user_logged_out
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
# Create your views here.
# Create your views here.
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.permissions import AllowAny
class UserApi(APIView):
    #permission_classes = []
    #authentication_classes = [] 
     

    permission_classes = [IsAuthenticated]

    def get(self,request,pk,*args,**kwargs):
        try:
            user = CustomUser.objects.get(pk=pk)
            return Response(UserSerializer(user).data,status= 200)
        except CustomUser.DoesNotExist:
            return Response(status=404,data="User Not Found")
    
    def put(self,request,pk):
     
        try :
            user = CustomUser.objects.get(pk=pk)
            serializer = UserSerializer(user,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=200)
            else :
                return Response(serializer.data,status=400)
        except :
            return Response("User Not Found!",status=404)
    
    def patch(self,request,pk):
       
        try :
            user = CustomUser.objects.get(pk=pk)
            serializer = UserSerializer(user,data = request.data , partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status= 200)
            else :
                return Response("Invalid Data!",status=400)
        except :
             return Response("User Not Found!",status=404)
