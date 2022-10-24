from dataclasses import fields
from pyexpat import model
from artists.models import Artists
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers


    
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Artists
        fields='__all__'