from django.contrib import admin
from albums.models import Album, Song


#thon man Register your models here.
class InlineSong(admin.StackedInline):
      model=Song
      extra=0
      min_num=1
class AlbumModel(admin.ModelAdmin):
      readonly_fields=('Creation_datetimee',)
      inlines=[InlineSong]     
admin.site.register(Album,AlbumModel)
admin.site.register(Song)
