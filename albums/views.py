from tkinter.tix import Form
from cgitb import html
from webbrowser import get
from django.http import HttpResponse
from django.shortcuts import render
from .models import Album
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse,Http404
from .forms import CreatAlbum

def new_album(request):
    #objects = MyUserManager()
   # artist=get_object_or_404(Artists,pk=Artist_name)
    form_album=CreatAlbum()
    #user=User.objects.first()
    if request.method =="POST":
        form_album=CreatAlbum(request.POST)
        if form_album.is_valid():
         form_album.save()
         
    else:
            form_album=CreatAlbum()
    return render(request,'new_album.html',{'form_album':form_album})
    
