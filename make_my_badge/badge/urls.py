from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^event/(?P<event_id>\d+)/list/$','make_my_badge.badge.views.item_list'),
)