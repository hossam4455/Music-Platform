from django.contrib import admin
from albums.models import Album


#thon man Register your models here.
class Albummodel(admin.ModelAdmin):
      readonly_fields=('Creationdatetimee',)
      
admin.site.register(Album,Albummodel)