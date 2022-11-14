from __future__ import absolute_import, unicode_literals
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
from dateutil.relativedelta import relativedelta
from django.conf import settings

@shared_task
def send_email_conglations(email_to,artist_name,name,cost):
   
    sleep(1)
    send_mail(
    f'conglations artist {artist_name}',
    f'for new album.{name}  cost : {cost}',
    'hossam.hssan47777@gmail.com',
    [email_to],
    fail_silently=False,
    )
    return None;     







def send_mail_func(user):
    if settings.EMAIL_HOST_USER:
        host_mail = f'name site <{settings.EMAIL_HOST_USER}>'
    else:
        host_mail = f'localServer <Admin@localServer.com>'

    mail_subject = "Hi! Artis"
    message = "please create album to get more followers"
    user.email_user(mail_subject, message,  host_mail) 





def check_between_two_dates(check_date):
    current_date = datetime.datetime.now().date()

    add_days = check_date + relativedelta(months=1)
    if add_days < current_date:
        return False

    return True





@shared_task
def check_albums(): 
 
    check_all_users = CustomUser.objects.all()
    if not check_all_users:
            # return HttpResponse(context, status=status.HTTP_201_CREATED)
            return


    for user in check_all_users:

        if not user.artist.artist_album.all():
            
            continue

        last_album = user.artist.artist_album.all()[0]
        check = check_between_two_dates(last_album.check_date)
        if not check:

            send_mail_func(user)
            last_album.check_date = datetime.datetime.now().date()
            last_album.save()
    # return HttpResponse(context, status=status.HTTP_201_CREATED)
    return

