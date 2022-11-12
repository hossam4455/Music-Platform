from asyncio.windows_events import NULL
from distutils.command.upload import upload
from email.mime import audio, image
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models import Model
from artists.models import Artists
from model_utils.fields import AutoCreatedField
from django.utils.translation import gettext_lazy as _
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

class TimeStampedModel(models.Model):

    Creation_datetimee = AutoCreatedField(_('Creation_datetimee'), null=False)
    check_date =  models.DateField(auto_now_add=True, null=False, verbose_name="hidden date") # new

    class Meta:
        abstract = True


class Album(TimeStampedModel):
    Artist_name = models.ForeignKey(Artists, on_delete=models.CASCADE, null=False, related_name = 'artist_album') #edit
    Album_name = models.CharField(max_length=200, default="New Album")
    Release_datetime = models.DateField(null=False)
    Cost = models.FloatField(blank=True,null=True)
    Is_approved = models.BooleanField(default=False, help_text=u" Approve the album if its name is not explicit")


    class Meta:
        # verbose_name = _("Album")
        # verbose_name_plural = _("Albums")
        ordering = ('-id',)        

    def __str__(self):
        return self.Album_name


    def clean(self):
        if self.Cost == None:pass
        else:
            if type(self.Cost) == float and self.Cost < 1:
                raise ValidationError({"Cost": _('Please enter value more than zero'), })


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=False, related_name = 'album_song')
    music_name = models.CharField(max_length=200,blank=True)
    image = models.ImageField(upload_to="images/")
    thumb = ProcessedImageField(upload_to="thumbs/",processors=[ResizeToFill(
        100, 50)], format='JPEG', options={'quality': 60}, blank=False)
    audio = models.FileField(upload_to="audios/",null=True, blank=True, validators=[
                             FileExtensionValidator(['mp3', 'wav'])])
   
 
    

  
    def __str__(self):
        return self.music_name 
    def clean(self):
        if len(self.music_name)<=0 or self.music_name=='':
            self.music_name=self.album.Album_name
