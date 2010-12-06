# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from apps.site import views

urlpatterns = patterns('',
    (r'^/*$', views.index_view),
    (r'^search/*$', views.search),
    (u'^(?P<need_type>[\w\s]+)/*$', views.list_view),
    (u'^(?P<need_type>[\w\s]+)/(?P<post_id>\d+)/*$', views.item_view),
    (r'^book/(?P<db_url>[\w\s]+)/(?P<id>[\w\d\\\\]+)/*$', views.book_view),
)
