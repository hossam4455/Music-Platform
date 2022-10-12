from tokenize import Name
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models import Model
from django.db.models import Count
from django.db.models import Q, Count



class Artists (models.Model):
  
   
    def Approved_Albums(self):
     return self.album_set.filter(Approved=True).count()
     
    def __str__(self) -> str:
     return self.Name
    Name = models.CharField(max_length=200, blank=False,
                            unique=True, null=False)
    Link = models.URLField(max_length=200, blank=True, null=False)
   