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
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator

    

class new_album(View):

    def get(self, request, *args, **kwargs):
        form_album=CreatAlbum()
        return render(request, 'new_album.html', {'form_album': form_album})

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
         form_album = CreatAlbum(request.POST)
        if form_album.is_valid():
          form_album.save()
        return redirect('new_albums')