from pyexpat import model
from django.contrib import admin
from artists.models import Artists
from albums.models import Album
from django.db.models import Count
from .models import *


class AlbumAdmin(admin.StackedInline):
    model = Album
    extra=1 
    
   


class AritstAdmin(admin.ModelAdmin):
    inlines = [AlbumAdmin]
    list_display=['Artist_name','Approved_Albums']
    def get_name(self, obj):
        return obj.Artists.Artist_name
   
   

admin.site.register(Artists, AritstAdmin)

# Register your models here.
# for artist in Artists.objects.all():
#    artist.album_set.all()
