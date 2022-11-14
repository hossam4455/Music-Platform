from tokenize import Name
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models import Model
from django.db.models import Count
from django.db.models import Q, Count
from users.models import CustomUser

class Artists (models.Model):

    Artist_name = models.CharField(max_length=200, blank=False,
                                   unique=True, null=False)
    user=models.OneToOneField(CustomUser, on_delete = models.CASCADE, related_name = 'artists')
    Artist_link = models.URLField(max_length=200, blank=True, null=False)




    def __str__(self) -> str:
        return self.Artist_name
