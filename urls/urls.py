# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from settings import PROJECT_ROOT

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^debug/', include('apps.btools.urls')),
    (r'^', include('apps.map.urls')),
    (r'^', include('apps.site.urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': PROJECT_ROOT + 'media', 'show_indexes': True}),
)
