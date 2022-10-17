from django.contrib import admin
from albums.models import Album


#thon man Register your models here.
class AlbumModel(admin.ModelAdmin):
      readonly_fields=('Creation_datetimee',)
      
admin.site.register(Album,AlbumModel)