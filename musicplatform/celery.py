from __future__ import absolute_import, unicode_literals
import os
import datetime
from celery import Celery



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'musicplatform.settings')

app = Celery('musicplatform')


app.config_from_object('django.conf:settings', namespace='CELERY')



app.autodiscover_tasks()
app.conf.broker_url = 'redis://localhost:6379/0'
