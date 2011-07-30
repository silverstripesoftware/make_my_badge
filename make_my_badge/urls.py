from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'make_my_badge.views.home', name='home'),
    # url(r'^make_my_badge/', include('make_my_badge.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
