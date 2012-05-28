# -*- coding: utf-8 -*-
from django.test import TestCase
from django.conf import settings

from models import Room

class Room_crud(TestCase):

    def test_create(self, test_name='first_test'):
        result = Room.objects.create(name=test_name,
                                     title='Test title',
                                     content = 'Test content',
                                     typograf_title='something about ',
                                     typograf_content='',
                                     views=777)
                                     
        self.assertEqual(result.__unicode__(), result.name)
        self.assertEqual(result.name, test_name)
        return result
        
    def test_read(self):
        rec = self.test_create('second_test')
        rec.save()
        find = Room.objects.get(name='second_test')
        self.assertEqual(find.name, 'second_test')        
        self.assertEqual(find.title, 'Test title')
        self.assertEqual(find.content, 'Test content')
        self.assertEqual(find.typograf_title, 'Test title')
        self.assertEqual(find.typograf_content, 'Test content')
        self.assertEqual(find.views, 777)
    
    def test_update(self):
        rec = self.test_create('third_test')
        rec.save()
        find = Room.objects.get(name='third_test')
        find.name += '_change'
        find.title += '_change'
        find.content += '_change'
        find.typograf_title += '_change'
        find.typograf_content += '_change'
        find.views = 666
        find.save()
        second = Room.objects.get(name='third_test_change')
        self.assertEqual(second.name, 'third_test_change')
        self.assertEqual(second.title, 'Test title_change')
        self.assertEqual(second.content, 'Test content_change')
        self.assertEqual(second.typograf_title, 'Test title_change')
        self.assertEqual(second.typograf_content, 'Test content_change')
        self.assertEqual(second.views, 666)
    
    
    def test_delete(self):
        rec = self.test_create('fourth_test')
        rec.save()
        find = Room.objects.get(name='fourth_test')
        find.delete()
