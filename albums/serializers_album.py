from dataclasses import fields
from pyexpat import model
from artists.models import Artists
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from users.models import CustomUser
from artists.serializers import ArtistSerializer
from albums.models import Album

    
class AlbumSerializer(serializers.ModelSerializer):
    Artist_name = ArtistSerializer(many=False,read_only=True)
    class Meta:
        model=Album
        fields=('Artist_name','Album_name','Release_datetime','Cost','Is_approved')
        
class AlbumCreateSeriakizer(serializers.ModelSerializer):
    
    class Meta:
        model=Album
        fields=( 'Album_name','Release_datetime','Cost','Is_approved')
            
        
    def validate(self, data):
        user = self.context['request']
        get_username = CustomUser.objects.get(username=user.username)
        data["Artist_name_id"] = get_username.id
        self.create(data)
        return True
        
    