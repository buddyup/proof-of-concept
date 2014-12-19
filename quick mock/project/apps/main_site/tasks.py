import datetime
from firebase import firebase
import requests
import uuid

from django.conf import settings
from django.core.cache import cache
from django.template.loader import render_to_string
from celery.task import task, periodic_task

from main_site.models import EventTombstone




@task(name="get_data")
def post_message(message):
    print settings.FIREBASE_KEY
    print message["body"]
    # message["timestamp"] = int(datetime.datetime.now().strftime("%s"))
    fb = firebase.FirebaseApplication('https://glowing-torch-3186.firebaseio.com',)
    # result = fb.put('/messages', uuid.uuid1(), message)
    # print result

    e = EventTombstone.objects.create()
    result = fb.patch('/status/events', {'count': EventTombstone.objects.count()})