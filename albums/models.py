from asyncio.windows_events import NULL
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models import Model
from artists.models import Artists
from model_utils.fields import AutoCreatedField
from django.utils.translation import gettext_lazy as _

class TimeStampedModel(models.Model):
    Creation_datetimee = AutoCreatedField(_('Creation_datetimee'),null=False)
    class Meta:
     abstract = True
   
class Album(TimeStampedModel):
    Artist_name = models.ForeignKey(Artists, on_delete=models.CASCADE,null=False)
    Album_name = models.CharField(max_length=200, default="New Album")
    Release_datetime = models.DateField(blank=False)
    Cost = models.FloatField(blank=True)
    Is_approved = models.BooleanField(default=False, help_text=u" Approve the album if its name is not explicit")
    def __str__(self):
     return self.Album_name
   



