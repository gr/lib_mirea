# -*- coding: utf-8 -*-

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-RU'


SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

APPEND_SLASH = True

#PROJECT_DIR = os.getcwd()
PROJECT_DIR = '/home/webadmin/lib_mirea_begin'

UPIMAGE_PATH = PROJECT_DIR +'/media/upimage'
UPIMAGE_URL = '/media/upimage'

UPIMAGE_THUMBNAIL_PATH = PROJECT_DIR + '/media/upimage/thumbnail'
UPIMAGE_THUMBNAIL_URL = '/media/upimage/thumbnail'

UPFILE_PATH = PROJECT_DIR + '/media/upfile'
UPFILE_URL = '/media/upfile'

TYPOGRAF_DIR = PROJECT_DIR + '/Typograf'


# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = PROJECT_DIR + '/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '^media/'


ROOT_URLCONF = 'urls.dev_gr_home'


Z3950_HOST = '10.0.86.222'
Z3950_PORT = 210
Z3950_DB = 'books'
Z3950_SYNTAX = 'RUSMARC'
Z3950_CHARSET = 'koi8-r'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin-media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'kgm6xqf8(d^#npksz--h@nm-p%#0gr1$ej6&0=atmb5ymsiucx'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_DIR + '/templates'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

INSTALLED_APPS = (
    'pytils',
    'apps.sorl.thumbnail',
    'apps.django_cron',
    'apps.map',
    'apps.Btools',
    'apps.site',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
)
