import simplejson
from django.template.response import TemplateResponse
from django.views.generic.list_detail import object_list
from django.http import HttpResponse

from badge.models import Item
from badge.tasks import generate_badge

def index(request):
    return TemplateResponse(request, "index.html", {})


def item_list(request,event_id):
    item_list = Item.objects.filter(event__id=int(event_id))
    return object_list(request, item_list, template_name="item_list.html", template_object_name="item")

def generate_badges(request,event_id):
    item_list = Item.objects.filter(event__id=int(event_id))
    for item in item_list:
        generate_badge.delay(item)
    r = HttpResponse()
    response_obj = {"statu":{"message":"ok"}}
    r.content = simplejson.dumps(response_obj)
    r["Content-Type"] = "application/json"
    r.status_code = 200
    return r