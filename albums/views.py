from tkinter.tix import Form
from cgitb import html
from webbrowser import get
from django.http import HttpResponse
from django.shortcuts import render
from .models import Album
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .forms import CreatAlbum
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from .serializers_album import AlbumSerializer, AlbumCreateSeriakizer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from django.core.paginator import Paginator
from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
import django_filters
from django_filters import rest_framework as filters


class new_album(View):

    def get(self, request, *args, **kwargs):
        form_album = CreatAlbum()

        return render(request, 'new_album.html', {'form_album': form_album})

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form_album = CreatAlbum(request.POST)
        if form_album.is_valid():
            form_album.save()
        return redirect('new_albums')


class LargeAlbumsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="Cost", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="Cost", lookup_expr='lte')
    name = filters.NumberFilter(field_name="Album_name", lookup_expr='iexact')

    class Meta:
        model = Album
        fields = ['min_price', 'max_price', 'name']


class AlbumCreat(generics.CreateAPIView):
    model = Album
    serializer_class = AlbumCreateSeriakizer
    permission_classes = [IsAdminUser]


class AlbumList(generics.ListAPIView):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAdminUser]
    pagination_class = LargeAlbumsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter


class AlbumListManule(generics.ListAPIView):
    serializer_class = AlbumSerializer


    def get_queryset(self):
       query = Album.objects.filter(Is_approved=True)
       try:
        query=query.filter(Album_name__iexact = self.request.GET['Album_name'])
       except: 
        pass
       try:
         
         cost = int(self.request.GET['Cost__gte'])
         query = query.filter(Cost__gte = cost)
       except KeyError:
         
         pass
       except:
         
         raise TypeError("Cost must be integer")
       try:
         
         cost=int(self.request.GET['Cost__lte'])
         query = query.filter(Cost__lte = cost )
       except KeyError:
         
         pass
       except:
         
         raise TypeError("Cost must be integer")
       return query
    
         
        
