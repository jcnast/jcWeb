# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Jul 25 2020, 13:03:44) 
# [GCC 8.3.0]
# Embedded file name: /Website/jcWeb/jcWeb/settings.py
# Compiled at: 2016-05-18 23:35:45
"""
Django settings for jcWeb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = '$ww85mnmtk^k@=!ww@@+%qn1iql^pv)c)d)x%#r6&60z0z#v=3'
DEBUG = False
TEMPLATE_DEBUG = False
TEMPLATE_DIRS = (
 os.path.join(BASE_DIR, 'templates'),)
ALLOWED_HOSTS = [
 'www.jaggernast.ca', 'localhost']
INSTALLED_APPS = ('django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes',
                  'django.contrib.sessions', 'django.contrib.messages', 'django.contrib.staticfiles',
                  'jcWeb')
MIDDLEWARE_CLASSES = ('django.contrib.sessions.middleware.SessionMiddleware', 'django.middleware.common.CommonMiddleware',
                      'django.middleware.csrf.CsrfViewMiddleware', 'django.contrib.auth.middleware.AuthenticationMiddleware',
                      'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
                      'django.contrib.messages.middleware.MessageMiddleware', 'django.middleware.clickjacking.XFrameOptionsMiddleware')
ROOT_URLCONF = 'jcWeb.urls'
WSGI_APPLICATION = 'jcWeb.wsgi.application'
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 
               'NAME': os.path.join(BASE_DIR, 'db.sqlite3')}}
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
STATICFILES_DIRS = (
 os.path.join(BASE_DIR, 'static'),
 'var/www/static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
MEDIAFILES_DIRS = (
 os.path.join(BASE_DIR, 'media'),
 'var/www/media')
# okay decompiling settings.pyc
