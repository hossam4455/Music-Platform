
import email
from rest_framework import serializers

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from users.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email','bio')
    