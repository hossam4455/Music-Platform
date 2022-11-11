from tkinter.tix import Form
from cgitb import html
from webbrowser import get
from django.http import HttpResponse
from django.shortcuts import render
from .models import Artists
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .forms import CreatArtist, ViweArtists
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import ArtistSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from artists import serializers
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
class view_artists(View):
  def get(self, request, *args, **kwargs):
    my_data_artist = Artists.objects.all()
    return render(request, 'artists.html', {'my_data_artist': my_data_artist})
 
####################





class MyFormView(View):
    template_name = 'artists.html'
    def get(self, request, *args, **kwargs):
        form_class =CreatArtist()
        return render(request, 'new_artist.html', {'form_class': form_class})

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
         form_class = CreatArtist(request.POST)
        if form_class.is_valid():
          form_class.save()
        return redirect('new_artist')

#class artists_list(APIView):
    
#  def get(self, request, *args, **kwargs): 
#  artist=Artists.objects.all()
#   data=ArtistSerializer(artist,many=True).data
#   return Response(data)
#  def post(self,request):
#        serializer=ArtistSerializer(data=request.data)
#        if serializer.is_valid():
#              serializer.save()
#              return Response(serializer.data,status=status.HTTP_201_CREATED)
#        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#to generics 
class ArtistsList(generics.ListCreateAPIView):
  
  queryset = Artists.objects.all()
  serializer_class=ArtistSerializer
  permission_classes = [IsAuthenticated]

           
            
           

 