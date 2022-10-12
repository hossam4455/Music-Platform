from pyexpat import model
from django.contrib import admin
from artists.models import Artists
from albums.models import Album
from django.db.models import Count
from .models import *


class albumAdmin(admin.StackedInline):
    model = Album
    extra=1 
    
   


class aritstAdmin(admin.ModelAdmin):
    inlines = [albumAdmin]
    list_display=['Name','Approved_Albums']
    def get_name(self, obj):
        return obj.Artists.Name
   
   

admin.site.register(Artists, aritstAdmin)

# Register your models here.
# for artist in Artists.objects.all():
#    artist.album_set.all()
