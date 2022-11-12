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

    @admin.display(description='Approved Albums')
    def get_approved_albums(self, obj):
        if not obj.artist_album.filter(Is_approved=True):
            return 0

        return obj.artist_album.filter(Is_approved=True).count()

    list_display=['Artist_name','get_approved_albums']
    def get_name(self, obj):
        return obj.Artists.Artist_name
   
   

admin.site.register(Artists, AritstAdmin)

# Register your models here.
# for artist in Artists.objects.all():
#    artist.album_set.all()
