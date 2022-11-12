from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth import get_user_model


# Create your models here.
class CustomUser(AbstractUser):

    username=models.CharField(max_length=255,null=False,unique=True,blank=False)
    email=models.CharField(max_length=255,unique=True,blank=False)
    password1=models.CharField(max_length=255,null=True,blank=False)
    password2=models.CharField(max_length=255,null=True,blank=False)
    bio = models.CharField(max_length=256,blank = True, null=True, default="")
    def __str__(self):
     return str(self.username)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    

 
