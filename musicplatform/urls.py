
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('albums/', include('albums.urls')),
    path('artists/', include('artists.urls')),
    path('admin/', admin.site.urls),
    path('',include('accounts.url'),name='home'),
    
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


