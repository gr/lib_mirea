# -*- coding: utf-8 -*-

from django.db.models import *
from django.conf import settings
from Typograf.typo import typografy
import Image as _Image


class Type(Model):
    id = AutoField(primary_key=True)
    name = CharField(u'Название', max_length=50)
    about = TextField(blank=True)

    def __unicode__(self):
        return self.name
        
    class Meta:
        verbose_name = u'Тип'
        verbose_name_plural = u'Типы'


class Post(Model):
    id = AutoField(primary_key=True)
    type = ForeignKey(Type, verbose_name=u'Тип поста')
    title = CharField(u'Заголовок', max_length=250, unique=True)
    content = TextField(u'Содержимое', blank=True)
    typograf_title = CharField(max_length=1000, default='none', editable=False)
    typograf_content = TextField(default='none', editable=False)
    date = DateTimeField(u'Дата', auto_now=True)
    event_date = DateField(u'Дата события (для объявлений)', default='1986-06-14')
    weight = IntegerField(u'Вес', default=0)
    views = IntegerField(u'Количество показов', default=0,editable=False)
    preview = TextField(u'Короткое содержимое', blank=True)
    typograf_preview = TextField(blank=True, editable=False)

    def __unicode__(self):
        return self.title

    def save(self):
        if self.preview == '':
            self.preview = self.content[:300]
        self.typograf_title = typografy(self.title)
        self.typograf_content = typografy(self.content)
        self.typograf_preview = typografy(self.preview)
        super(Post, self).save()      

    class Meta:
        verbose_name = u'Пост'
        verbose_name_plural = u'Посты'

        
class Image(Model):
    name = CharField(u'Название (лучше латиницей)',max_length=50)
    img = ImageField(u'Путь к картинке' ,upload_to=settings.UPIMAGE_PATH)
    img_url = CharField(u'Адрес картинки', max_length=1050, editable=False, blank=True)
    thumbnail = ImageField(upload_to=settings.UPIMAGE_THUMBNAIL_PATH, editable=False, blank=True)
    thumbnail_url = CharField(u'Адрес миниатюры', max_length=1050, editable=False, blank=True)
    weight = IntegerField(u'Ширина', default=90)
    height = IntegerField(u'Высота', default=90)

    def save(self):
        super(Image, self).save()
        size = self.weight, self.height
        buf = self.img.path.split('/')
        file_name = buf.pop(len(buf)-1)
        self.img_url = settings.UPIMAGE_URL+'/'+file_name
        img = _Image.open(self.img.path)
        img.quality = 100
        img.thumbnail(size, _Image.ANTIALIAS)
        thumbnail_path = settings.UPIMAGE_THUMBNAIL_PATH+'/'+file_name
        img.save(thumbnail_path)
        self.thumbnail = thumbnail_path
        self.thumbnail_url = settings.UPIMAGE_THUMBNAIL_URL+'/'+file_name
        super(Image, self).save()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Картинка'
        verbose_name_plural = u'Картинки'


class File(Model):
    name = CharField(u'Название', max_length=50)
    file_path = FileField(u'Путь к файлу на сервере', upload_to=settings.UPFILE_PATH)
    file_url = CharField(u'Путь к файлу на сайте', max_length=1050, editable=False, blank=True)
    
    def save(self):
        buf = self.file_path.path.split('/')
        self.file_url = settings.UPFILE_URL +'/'+ buf.pop(len(buf)-1)
        super(File, self).save()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Файл'
        verbose_name_plural = u'Файлы'        

