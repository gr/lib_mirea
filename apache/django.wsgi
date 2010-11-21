import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.world'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
sys.path.append('/home/webadmin/lib_mirea_begin')
