from django_celery_beat.apps import BeatConfig
from django_celery_beat.models import (
    PeriodicTask, PeriodicTasks,
    IntervalSchedule, CrontabSchedule,
    SolarSchedule, ClockedSchedule
)


BeatConfig.verbose_name = "ssssssss"

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('albums/', include('albums.urls')),
    path('artists/', include('artists.urls')),
    path('admin/', admin.site.urls),
    path('',include('accounts.url'),name='home'),
    path('api-auth/', include('rest_framework.urls')),
    
    path('api/', include('authentication.urls')),

    path(r'api/auth/', include('knox.urls')),
    path('users/', include('users.urls')),
    
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


 