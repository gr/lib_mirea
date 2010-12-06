# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from models import Room

'''
in:
out:
'''
def map_render(request, **kwargs):
    if kwargs.has_key('room_name'):
        room = get_object_or_404(Room, name=kwargs['room_name'])
        room.views+=1
        room.save()
    return render_to_response(kwargs['tpl'], locals())
