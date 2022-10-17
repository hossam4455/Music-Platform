from dataclasses import fields
from pyexpat import model
from .models import Album
from django import forms
class CreatAlbum(forms.ModelForm):
    class Meta:
        model=Album
        fields=['Artist_name','Album_name','Release_datetime','Cost','Is_approved']
            
    
    