import simplejson
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list_detail import object_list
from django.http import HttpResponse

from badge.models import Item, Event
from badge.tasks import generate_badge

def event_list(request):
    event_list = Event.objects.filter(user=request.user)
    return object_list(request, event_list, template_name="event_list.html", template_object_name="event")

def item_list(request,event_id):
    item_list = Item.objects.filter(event__id=int(event_id))
    return object_list(request, item_list, template_name="item_list.html", template_object_name="item")

@csrf_exempt
def generate_badges(request,event_id):
    item_list = Item.objects.filter(event__id=int(event_id))
    for item in item_list:
        generate_badge.delay(item)
    r = HttpResponse()
    response_obj = {"status":{"message":"ok"}}
    r.content = simplejson.dumps(response_obj)
    r["Content-Type"] = "application/json"
    r.status_code = 200
    return r

def are_badges_ready(request,event_id):
    e = Event.objects.get(id=int(event_id))
    item_count = Item.objects.filter(event=e,generated_image="").count()
    ready = True
    if item_count > 0:
        ready = False

    response_obj = {"status":{"ready":ready}}
    r = HttpResponse()
    r.content = simplejson.dumps(response_obj)
    r["Content-Type"] = "application/json"
    r.status_code = 200
    return r


