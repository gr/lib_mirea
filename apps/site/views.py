# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from models import *
from apps.map.models import *
from ZClient.ZClient import ZClient
from django.db.models import Q
from apps.Btools.models import BookSet

def index_view(request):
    news = Post.objects.filter(type=get_object_or_404(Type, name='Объявления').id).order_by('-event_date','-weight','-views')[:6]
    infos = Post.objects.filter(type=get_object_or_404(Type, name='Справка').id).order_by('-weight')[:4]
    abouts = Post.objects.filter(type=get_object_or_404(Type, name='О библиотеке').id).order_by('-weight')[:4]
    last_books = BookSet.objects.get( name = 'Новые поступления')
    return render_to_response('index.html', locals())

def list_view(request, need_type):
    need_type = get_object_or_404(Type, name=need_type)
    if need_type.name == u'Объявления': items = Post.objects.filter(type=4).order_by('-event_date','-weight','-views')[:7] #,event_date__gte=date.today()-timedelta(days=90)
    else: items = Post.objects.filter(type=need_type.id).order_by('-weight','-views')
    booksets = BookSet.objects.filter( view_me=True )
    return render_to_response('list.html', locals())

def item_view(request, need_type, post_id):
    need_type = get_object_or_404(Type, name=need_type)
    item = get_object_or_404(Post, id=int(post_id), type=need_type.id)
    Post.objects.filter(id=item.id).update(views=item.views+1)
    if need_type.id == 4: menu = Post.objects.filter(type=4).order_by('-event_date','-weight','-views')[:7]
    else: menu = Post.objects.filter(type=need_type.id).order_by('-weight','-views')
    return render_to_response('item.html', locals())

def search(request):
    page='search'
    remote_ip = request.META.get('REMOTE_ADDR')
    if '10.0.86' in remote_ip:
        ip_status = 'local'
    else:
        ip_status = 'remote'
    if request.GET.get('search_field', 0) != 0 and request.GET['search_field'].strip() != '':
        keyword = request.GET['search_field'].strip()[:120] # 250 + <wbr> 
        if keyword in ['for', 'in', 'else', 'if', 'and', 'not', 'or', 'where', 'from', 'by', 'as', '""'] or '"' in keyword:
            message = '4'
        elif len(keyword) < 2:
            message = '2'
        else:
            items = Post.objects.filter(Q(title__icontains=keyword)|Q(content__icontains=keyword)).order_by('-type')
            rooms = Room.objects.filter(Q(title__icontains=keyword)|Q(content__icontains=keyword)|Q(name__icontains=keyword))
            try:
                search = ZClient()
                search.connect('10.0.86.222',210,'books','RUSMARC','koi8-r')
                books, b_len = search.get_books(keyword, length=100)
                if '10.0.86' in remote_ip:
                    search.set_db('ebooks')
                    ebooks, eb_len = search.get_books(keyword, length=100)
                search.set_db('share')
                share_books, shb_len = search.get_books(keyword, length=100)
            except:
                books, b_len = [], 0
                ebooks, eb_len = [], 0
                share_books, shb_len = [], 0
            if len(books) == b_len: b_len=0
            if len(ebooks) == eb_len: eb_len=0
            if len(share_books) == shb_len: shb_len=0
            if len(items)==0 and len(rooms)==0 and len(books)==0 and len(ebooks)==0:
                message = '3'
    else:
        message = '1'
    return render_to_response('search.html', locals())
