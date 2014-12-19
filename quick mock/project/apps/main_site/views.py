import json
import requests

from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string

from annoying.decorators import render_to, ajax_request
from main_site.models import DataPoint, Milestone, Sale, poc_DATA_KEY
from main_site.tasks import post_message

@render_to("main_site/home.html")
def home(request):
    
    return locals()


@ajax_request
@csrf_exempt
def chat_posted(request):
    try:
        data = json.loads(request.body)
        if "body" in data:
            post_message.delay(data)
            # post_message(data)
            return {"success": True}
    except:
        import traceback; traceback.print_exc();
        pass
    return {"success": False}