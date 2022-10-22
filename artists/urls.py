from django.urls import path
from django.urls import path
from . import views
from .views import view_artists
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView

urlpatterns = [

    path('create/', views.MyFormView.as_view(), name='new_artist'),

    path('', views.view_artists.as_view(), name='view_artists')
]
