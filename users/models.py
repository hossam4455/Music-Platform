from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth import get_user_model


# Create your models here.
class CustomUser(AbstractUser):
       
    username=models.CharField(max_length=255,null=True,unique=True)
    email=models.CharField(max_length=255,unique=True)
    password1=models.CharField(max_length=255,null=True)
    password2=models.CharField(max_length=255,null=True)
    bio = models.CharField(max_length=256,blank = True, null=False, default="")
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
 

    