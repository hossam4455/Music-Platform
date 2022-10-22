from dataclasses import fields
from pyexpat import model
from .models import Artists
from django import forms


class CreatArtist(forms.ModelForm):
    class Meta:
        model = Artists
        fields = ['Artist_name', 'Artist_link']


class ViweArtists(forms.ModelForm):
    class Meta:
        model = Artists
        fields = []
