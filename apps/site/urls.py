# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from apps.site import views

urlpatterns = patterns('',
    (r'^/*$', views.index_view),
    (r'^search/*$', views.search),
    (u'^(?P<need_type>(Ресурсы|Справка|Объявления|О библиотеке))/*$', views.list_view),
    (u'^(?P<need_type>(Ресурсы|Справка|Объявления|О библиотеке))/(?P<post_id>\d+)/*$', views.item_view),
    (r'^(?P<db_url>(bgu|books|ebooks|share))/(?P<book_id>[\w\d\\\\]+)/*$', views.book_view),
)
