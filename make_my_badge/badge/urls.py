from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$','make_my_badge.badge.views.event_list', name="event_list"),
    url(r'^event/(?P<event_id>\d+)/$','make_my_badge.badge.views.item_list', name="item_list"),
    url(r'^event/(?P<event_id>\d+)/generate/$','make_my_badge.badge.views.generate_badges', name="generate_badges"),
    url(r'^event/(?P<event_id>\d+)/are_badges_ready/$','make_my_badge.badge.views.are_badges_ready', name="are-badges-ready"),
)