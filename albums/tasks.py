from time import sleep
from django.core.mail import send_mail
from celery import shared_task
from celery import Celery
from celery.schedules import crontab
from musicplatform import settings
from django.utils import timezone
from datetime import timedelta
from users.models import CustomUser
from artists.models import Artists
from albums.models import Album
from django.contrib.auth import get_user_model
import datetime
@shared_task()
def send_email_celery(email_to,artist_name,album_name,cost):
    """Sends an email when the feedback form has been submitted."""
    sleep(1)  # Simulate expensive operation(s) that freeze Django
    send_mail(
    f'conglations artist {artist_name}',
    f'for new album. {album_name} cost : {cost}',
    'hossam.hssan47777@gmail.com',
    [email_to],
    fail_silently=False,
    )
    return None;     
@shared_task(bind=True)
def send_mail_func(self,request):
    time_thresold=datetime.now() -datetime.timedelta(hours=2)
    self.artists.album.object.last(user=request.user)
    artists = CustomUser.objects.all()
    #timezone.localtime(users.date_time) + timedelta(days=2)
    for artist in artists:
        mail_subject = "Hi! Artis"
        message = "please create album to get more followers"
        Album.object.last(user=request.user)
        to_email = CustomUser.email
        send_mail(
            subject = mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=False,
        )
    return "Done"
