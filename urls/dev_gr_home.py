# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

from apps import django_cron
django_cron.autodiscover()

urlpatterns = patterns('',

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    
    (r'^book/(?P<id>\d+)/*$', 'apps.Btools.views.get_book', {'db':'books', 'tpl':'record.html'}),
    (r'^ebook/(?P<id>\d+)/*$', 'apps.Btools.views.get_book', {'db':'ebooks', 'tpl':'record.html'}),
    (r'^share/(?P<id>\d+)/*$', 'apps.Btools.views.get_book', {'db':'share', 'tpl':'record.html'}),

    (r'^test/(?P<id>\d+)/*$', 'apps.Btools.views.get_book', {'db':'books', 'tpl':'debug.html', 'debug': 'on'}),
    (r'^etest/(?P<id>\d+)/*$', 'apps.Btools.views.get_book', {'db':'ebooks', 'tpl':'debug.html', 'debug': 'on'}),
    
    ( settings.MEDIA_URL+'(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    (r'^/*$', 'apps.site.views.index_view'),

    (r'^search/*$', 'apps.site.views.search'),

    (u'^Схема/Комната/(?P<room_name>(\d+|cat))/*$', 'apps.map.views.map_render', {'tpl': 'map-ajax.html'}),
    (u'^Схема/(?P<room_name>(\d+|cat))/*$', 'apps.map.views.map_render', {'tpl': 'map.html'}),
    (u'^Схема/*$', 'apps.map.views.map_render', {'tpl': 'map.html'}),

    (u'Набор/*$', 'apps.Btools.views.bookset_index', {'tpl':'list.html'}),
    (u'Набор/(?P<bookset>[\w\s]*)/*$', 'apps.Btools.views.bookset', {'tpl':'bookset.html'}), # в шаблоне всего одна переменная bookset, поля расписаны в шаблоне bookset_index.html + массив книжек bookset.books

    (r'^query/*$', 'apps.Btools.views.query', {'tpl':'debug-query.html'}),
    
    #    for lists
    (u'^(?P<need_type>[\w\s]*)/*$', 'apps.site.views.list_view'),
    #    for items
    (u'^(?P<need_type>[\w\s]*)/(?P<post_id>\d+)/*$', 'apps.site.views.item_view'),

)
