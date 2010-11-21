# -*- coding: utf-8 -*-

from django.db.models import *
from django.conf import settings
from Typograf.typo import typografy


class Room(Model):
    id = AutoField(primary_key=True)
    name = CharField(u'Номер', max_length=50, unique=True)
    title = CharField(u'Заголовок', max_length=250, blank=True)
    content = TextField(u'Содержимое', blank=True)
    typograf_title = CharField(max_length=1000, default='none', editable=False)
    typograf_content = TextField(default='none', editable=False)
    views = IntegerField(u'Количество просмотров', default=0,editable=False)

    def save(self):
        if settings.TYPOGRAFY:
            self.typograf_title = typografy(self.title)
            self.typograf_content = typografy(self.content)
        else:
            self.typograf_title = self.title
            self.typograf_content = self.content
        super(Room, self).save()

    def __unicode__(self):
        return self.name
        
    class Meta:
        verbose_name = u'Комната'
        verbose_name_plural = u'Комнаты'
