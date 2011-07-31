from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'badge.views.index', name='index'),
    url(r'^badge/', include('make_my_badge.badge.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
