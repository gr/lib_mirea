# -*- coding: utf-8 -*-

from settings.dev_base_settings import *

DATABASE_ENGINE = 'mysql'			# 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'lib_mirea_begin'	# Or path to database file if using sqlite3.
DATABASE_USER = 'root'				# Not used with sqlite3.
DATABASE_PASSWORD = 'qazikmysql'	# Not used with sqlite3.
DATABASE_HOST = ''					# Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''					# Set to empty string for default. Not used with sqlite3.

TYPOGRAFY = False					# Or True to activate Typograf

DEBUG = False

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS
