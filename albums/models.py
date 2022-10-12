from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models import Model
from artists.models import Artists


class Album(models.Model):
 
    def __str__(self):
          return self.Albumname
    Artistname = models.ForeignKey(Artists, on_delete=models.CASCADE)
    Albumname = models.CharField(max_length=200, default="New Album")
    Creationdatetimee = models.DateField()
    Releasedatetime = models.DateField()
    Cost = models.FloatField(blank=True)
    Approved = models.BooleanField(default=False, help_text=u" Approve the album if its name is not explicit")
   



