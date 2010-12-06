# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from apps.map import views

urlpatterns = patterns('',
    (u'^Схема/Комната/(?P<room_name>(\d+|cat))/*$', views.map_render, {'tpl': 'map-ajax.html'}),
    (u'^Схема/(?P<room_name>(\d+|cat))/*$', views.map_render, {'tpl': 'map.html'}),
    (u'^Схема/*$', views.map_render, {'tpl': 'map.html'}),
)
