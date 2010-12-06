from django.contrib import admin
from models import Room

class RoomAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
#    list_filter = ['type']
    ordering = ['name']
    list_display = ('name', 'title', 'views')
    
admin.site.register(Room, RoomAdmin)
