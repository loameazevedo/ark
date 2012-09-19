"""Settings for Development Server"""
import os

from src.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'uploads')
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'ark.db'),
    }
}

# WSGI_APPLICATION = '{{ project_name }}.wsgi.dev.application'
