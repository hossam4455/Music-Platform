from lib2to3.pgen2 import token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import RegisterSerializer
from users.models import CustomUser
import jwt, datetime
from rest_framework.decorators import api_view
from rest_framework import generics, permissions, serializers
from rest_framework import generics
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from rest_framework.authentication import BasicAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializers import  RegisterSerializer, LoginSerializer,UserSerializer,sigSerializer
from knox.auth import TokenAuthentication
from .models import User
from django.utils import timezone
from rest_framework import status
from django.contrib.auth.signals import user_logged_in, user_logged_out
from rest_framework.permissions import IsAuthenticated
# Create your views here.
#class RegisterView(APIView):
#    def post(self, request):
#        serializer = UserSerializer(data=request.data)
#        serializer.is_valid(raise_exception=True)
#        serializer.save()
#        return Response(serializer.data)

class RegisterView(generics.ListCreateAPIView):
      queryset = CustomUser.objects.all()
      serializer_class=RegisterSerializer
class SignInAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer
  
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": sigSerializer(user).data,
            "token": AuthToken.objects.create(user)[1],
            
        })
