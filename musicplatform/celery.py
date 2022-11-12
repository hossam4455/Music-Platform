# # django_celery/celery.py

# import os
# from celery import Celery
# from django.conf import settings
# from celery.schedules import crontab
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "musicplatform.settings")
# app = Celery("musicplatform")
# app.config_from_object("django.conf:settings", namespace="CELERY")
# app.conf.enable_utc = False
# app.conf.update(timezone = 'Africa/Cairo')
# # app.conf.beat_schedule = {
# #     'send-mail-every-day-at-8': {
# #         'task': 'send_mail_app.tasks.send_mail_func',
# #         'schedule': crontab(hour=16, minute=4),
# #         #'args': (2,)
# #     }
    
# # }

# app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')
# app.autodiscover_tasks()

##############################################################
##############################################################
##############################################################
##############################################################

from __future__ import absolute_import, unicode_literals

import os
import datetime
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'musicplatform.settings')

app = Celery('musicplatform')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
app.conf.broker_url = 'redis://localhost:6379/0'
# app.now = datetime.datetime.now




# import os
# from celery import Celery

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'musicplatform.settings')

# app = Celery('musicplatform')

# app.config_from_object('django.conf:settings', namespace='CELERY')

# # Load task modules from all registered Django apps.
# app.autodiscover_tasks()