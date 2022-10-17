from tkinter.tix import Form
from cgitb import html
from webbrowser import get
from django.http import HttpResponse
from django.shortcuts import render
from .models import Artists
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse,Http404
from .forms import CreatArtist, ViweArtists

def new_artist(request):
    #objects = MyUserManager()
   # artist=get_object_or_404(Artists,pk=Artist_name)
    form=CreatArtist()
    #user=User.objects.first()
    if request.method =="POST":
        form=CreatArtist(request.POST)
        if form.is_valid():
         form.save(commit=False)
         
    else:
            form=CreatArtist()
    return render(request,'new_artist.html',{'form':form})
def view_artists(request):
    my_data_artist=Artists.objects.all()
    context={
      'my_data_artist':my_data_artist,
    } 

    return render(request, 'artists.html', context)