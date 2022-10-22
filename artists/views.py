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


class view_artists(View):
  def get(self, request, *args, **kwargs):
    my_data_artist = Artists.objects.all()
    return render(request, 'artists.html', {'my_data_artist': my_data_artist})
 
####################




@method_decorator(login_required, name='dispatch')
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

           

 