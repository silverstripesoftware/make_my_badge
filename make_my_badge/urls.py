from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
    url(r'^badge/', include('badge.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # make django serve the uploaded files path in development
    urlpatterns += patterns('',
        url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
