# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from apps.site import views

urlpatterns = patterns('',
    (u'^/*$', views.index_view),
    (u'^search/*$', views.search),
    (u'^(?P<need_type>(Ресурсы|Справка|Объявления|О библиотеке))/*$', views.list_view),
    (u'^(?P<need_type>(Ресурсы|Справка|Объявления|О библиотеке))/(?P<post_id>\d+)/*$', views.item_view),
    (u'^Ресурсы/(?P<bookset_name>[\w\d\s]+)/*$', views.bookset_view),
    (u'^(?P<db_url>(bgu|books|ebooks|share))/(?P<book_id>[\w\d\\\\]+)/*$', views.book_view),
)
