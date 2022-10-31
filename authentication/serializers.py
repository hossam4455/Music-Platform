import email
from rest_framework import serializers

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser

        fields = ['id', 'username', 'email', 'password1', 'password2']
        extra_kwargs = {
            'password1': {'write_only': True},
            'password2': {'write_only': True}
        }

    def create(self, validated_data):
       # CustomUser.objects.create_user(username=validated_data(
         #   'username'), password1=validated_data('password1'), email=validated_data('email'))
         
        password1 = validated_data.pop('password1', None)
        instance = self.Meta.model(**validated_data)
        if password1 is not None:
            instance.set_password(password1)
        instance.save()
        return instance

    def validate_email(self, email):
        existing = CustomUser.objects.filter(email=email).first()
        if existing:
            raise serializers.ValidationError("Someone with that email "
                                              "address has already registered. Was it you?")
        return email

    def validate(self, data):
        if not data.get('password1') or not data.get('password2'):
            raise serializers.ValidationError("Please enter a password and "
                                              "confirm it.")
        if data.get('password1') != data.get('password2'):
            raise serializers.ValidationError("Those passwords don't match.")
        return data
class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials Passed.')


class sigSerializer(serializers.Serializer):

    username = serializers.CharField()

    bio = serializers.CharField()
    email = serializers.CharField()
