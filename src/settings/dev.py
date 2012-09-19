"""Settings for Development Server"""
import os

from src.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

VAR_ROOT = '/var/www/openchurch'
MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')
STATIC_ROOT = os.path.join(VAR_ROOT, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'openchurch',
#        'USER': 'dbuser',
#        'PASSWORD': 'dbpassword',
    }
}

# WSGI_APPLICATION = '{{ project_name }}.wsgi.dev.application'
