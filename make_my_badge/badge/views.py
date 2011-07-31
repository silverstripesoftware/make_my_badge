from django.template.response import TemplateResponse
from django.views.generic.list_detail import object_list

from badge.models import Item

def index(request):
    return TemplateResponse(request, "index.html", {})


def item_list(request,event_id):
    item_list = Item.objects.filter(event__id=int(event_id))
    return object_list(request, item_list, template_name="item_list.html", template_object_name="item")