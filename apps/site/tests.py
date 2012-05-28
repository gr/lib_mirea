# -*- coding: utf-8 -*-
from django.test import TestCase
from django.conf import settings

from models import Type, Post, Image, File

class Type_crud(TestCase):

    def test_create(self, test_name='First_test'):
        result = Type.objects.create(name=test_name,
                                     about='Something about')
        
        self.assertEqual(result.__unicode__(), result.name)
        self.assertEqual(result.name, test_name)
        return result
        
    def test_read(self):
        rec = self.test_create('Second_test')
        rec.save()
        find = Type.objects.get(name='Second_test')
        self.assertEqual(find.name, 'Second_test')
        self.assertEqual(find.about, 'Something about')
        self.assertEqual(find.id, 5)
    
    def test_update(self):
        rec = self.test_create('Third_test')
        rec.save()
        find = Type.objects.get(name='Third_test')
        find.name += '_change'
        find.about += '_change'
        find.save()
        second = Type.objects.get(name='Third_test_change')
        self.assertEqual(second.name, 'Third_test_change')
        self.assertEqual(second.about, 'Something about_change')
        self.assertEqual(second.id, 5)
    
    def test_delete(self):
        rec = self.test_create('Fourth_test')
        rec.save()
        find = Type.objects.get(name='Fourth_test')
        find.delete()
  
        
class Post_crud(TestCase):

    def test_create(self, test_name='First_test'):
        result = Post.objects.create(type=Type.objects.get(name=u'Объявления'),
                                     title=test_name,
                                     content = 'Test content',
                                     preview='Test preview')
        
        self.assertEqual(result.__unicode__(), result.title)
        self.assertEqual(result.title, test_name)
        return result
        
    def test_read(self):
        rec = self.test_create('Second_test')
        rec.save()
        find = Post.objects.get(title='Second_test')
        self.assertEqual(find.title, 'Second_test')
        self.assertEqual(find.typograf_title, 'Second_test')
        self.assertEqual(find.content, 'Test content')
        self.assertEqual(find.typograf_content, 'Test content')
        self.assertEqual(find.preview, 'Test preview')
        self.assertEqual(find.typograf_preview, 'Test preview')
        self.assertEqual(find.views, 0)
        self.assertEqual(find.weight, 0)
        self.assertEqual(find.type.name, u'Объявления')
        #self.assertEqual(find.date, 0)
        #self.assertEqual(find.event_date, 0)
    
    def test_update(self):
        rec = self.test_create('Third_test')
        rec.save()
        find = Post.objects.get(title='Third_test')
        find.title += '_change'
        find.content += '_change'
        find.preview += '_change'
        find.views += 777
        find.weight += 666
        find.type = Type.objects.get(name=u'Ресурсы')
        #find.date += '_change'
        #find.event_date += '_change'
        find.save()
        second = Post.objects.get(title='Third_test_change')
        self.assertEqual(second.title, 'Third_test_change')
        self.assertEqual(second.typograf_title, 'Third_test_change')
        self.assertEqual(second.content, 'Test content_change')
        self.assertEqual(second.typograf_content, 'Test content_change')
        self.assertEqual(second.preview, 'Test preview_change')
        self.assertEqual(second.typograf_preview, 'Test preview_change')
        self.assertEqual(second.views, 777)
        self.assertEqual(second.weight, 666)
        self.assertEqual(second.type.name, u'Ресурсы')
        #self.assertEqual(second.date, 0)
        #self.assertEqual(second.event_date, 0)
    
    def test_delete(self):
        rec = self.test_create('Fourth_test')
        rec.save()
        find = Post.objects.get(title='Fourth_test')
        find.delete()


class Image_crud(TestCase):

    def test_create(self, test_name='first_test'):
        result = Image.objects.create(name=test_name,
                                      img = settings.UPIMAGE_PATH + '/../img/wow.png'
                                     )
        
        self.assertEqual(result.__unicode__(), result.name)
        self.assertEqual(result.name, test_name)
        return result
        
    def test_read(self):
        rec = self.test_create('Second_test')
        rec.save()
        find = Image.objects.get(name='Second_test')
        self.assertEqual(find.name, 'Second_test')
        self.assertEqual(find.img, settings.UPIMAGE_PATH + '/../img/wow.png')
        self.assertEqual(find.img_url, '/media/upimage/wow.png')
        self.assertEqual(find.thumbnail, settings.UPIMAGE_THUMBNAIL_PATH + '/wow.png')
        self.assertEqual(find.thumbnail_url, '/media/upimage/thumbnail/wow.png')
        self.assertEqual(find.weight, 90)
        self.assertEqual(find.height, 90)
    
    def test_update(self):
        rec = self.test_create('Third_test')
        rec.save()
        find = Image.objects.get(name='Third_test')
        find.name += '_change'
        find.img = settings.UPIMAGE_PATH + '/../img/you.jpg'
        find.height += 10
        find.weight += 10
        find.save()
        second = Image.objects.get(name='Third_test_change')
        self.assertEqual(second.name, 'Third_test_change')
        self.assertEqual(second.height, 100)
        self.assertEqual(second.weight, 100)
        self.assertEqual(second.img, settings.UPIMAGE_PATH + '/../img/you.jpg')
        self.assertEqual(second.img_url, '/media/upimage/you.jpg')
        self.assertEqual(second.thumbnail, settings.UPIMAGE_THUMBNAIL_PATH + '/you.jpg')
        self.assertEqual(second.thumbnail_url, '/media/upimage/thumbnail/you.jpg')
    
    def test_delete(self):
        rec = self.test_create('Fourth_test')
        rec.save()
        find = Image.objects.get(name='Fourth_test')
        find.delete()


class File_crud(TestCase):

    def test_create(self, test_name='first_test'):
        result = File.objects.create(name=test_name,
                                     file_path = settings.UPFILE_PATH + '/../img/wow.png'
                                     )
        
        self.assertEqual(result.__unicode__(), result.name)
        self.assertEqual(result.name, test_name)
        return result
        
    def test_read(self):
        rec = self.test_create('Second_test')
        rec.save()
        find = File.objects.get(name='Second_test')
        self.assertEqual(find.name, 'Second_test')
        self.assertEqual(find.file_path, settings.UPFILE_PATH + '/../img/wow.png')
        self.assertEqual(find.file_url, '/media/upfile/wow.png')
    
    def test_update(self):
        rec = self.test_create('Third_test')
        rec.save()
        find = File.objects.get(name='Third_test')
        find.name += '_change'
        find.file_path = settings.UPFILE_PATH + '/../img/you.jpg'
        find.save()
        second = File.objects.get(name='Third_test_change')
        self.assertEqual(second.name, 'Third_test_change')
        self.assertEqual(second.file_path, settings.UPFILE_PATH + '/../img/you.jpg')
        self.assertEqual(second.file_url, '/media/upfile/you.jpg')
        
    def test_delete(self):
        rec = self.test_create('Fourth_test')
        rec.save()
        find = File.objects.get(name='Fourth_test')
        find.delete()
