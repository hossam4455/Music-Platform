from django.urls import path
from .views import UserApi#,check_albums

urlpatterns = [
    path("<int:pk>/" , UserApi.as_view(),name="userApi"),


    # path('check_albums/', check_albums, name='check_albums'),
]