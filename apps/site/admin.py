# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Post, Type, Image, File

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
    list_filter = ['type']
    ordering = ['type']
    list_display = ('title', 'type', 'weight', 'views', 'date')

class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'about')

class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'img_url','thumbnail_url')

class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'file_path', 'file_url')

admin.site.register(Post, PostAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(File, FileAdmin)

