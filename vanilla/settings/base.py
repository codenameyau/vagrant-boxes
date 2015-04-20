"""
Django base settings

DESCRIPTION:
This file contains common settings between the development and
production environments. Feel free to add additional settings
files for staging and testing.

SECURITY:
Your django SECRET_KEY will be autogenerated in 'secrets.json'.
Password sensitive settings and API keys should go into 'secrets.py'.

More information on the Django settings file:
https://docs.djangoproject.com/en/1.7/topics/settings/
https://docs.djangoproject.com/en/1.7/ref/settings/

Django Extensions Commands:
http://django-extensions.readthedocs.org/en/latest/command_extensions.html
"""

################################################################
# BASE APPLICATION SETTINGS
################################################################
DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PLUGIN_APPS = [
    'grappelli',
    'braces',
    'django_extensions',
    'django.contrib.admin',
]

PROJECT_APPS = [
    'vanilla.apps.core',
    'vanilla.apps.website',
]

INSTALLED_APPS = DJANGO_APPS + PLUGIN_APPS + PROJECT_APPS


################################################################
# BASE CONFIGURATION SETTINGS
################################################################

# Django root urls file
ROOT_URLCONF = 'vanilla.urls'

# WSGI application
WSGI_APPLICATION = 'vanilla.wsgi.application'

# Debug settings
DEBUG = False
TEMPLATE_DEBUG = False

# Site URL extras
APPEND_SLASH = True
PREPEND_WWW = False

# Specifiy hosts
ALLOWED_HOSTS = [
    'localhost'
]


################################################################
# BASE DIRECTORY SETTINGS
################################################################
from unipath import Path

# Same directory as `manage.py`
BASE_DIR = Path(__file__).ancestor(3)
STATIC_URL  = '/static/'
MEDIA_URL   = '/media/'

STATICFILES_DIRS = (
    BASE_DIR.child('static'),
)

################################################################
# BASE MIDDLEWARE SETTINGS
################################################################
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)


################################################################
# BASE SECRETS SETTINGS
################################################################
from django.core.exceptions import ImproperlyConfigured as ICONFIG
from vanilla.settings.secrets import *
from json import loads as loadjson

try:
    with open('secrets.json') as fp:
        SECRETS = loadjson(fp.read())
        SECRET_KEY = SECRETS['SECRET_KEY']
except IOError:
    raise ICONFIG('File not found: secrets.json')
except KeyError:
    raise ICONFIG('SECRET_KEY is not defined.')


################################################################
# BASE AUTHENTICATION SETTINGS
################################################################

# The model to use to represent a User.
AUTH_USER_MODEL = 'auth.User'

# The URL where requests are redirected for login.
# LOGIN_URL = '/accounts/login/'

# The URL where requests are redirected for logout.
# LOGOUT_URL = '/accounts/logout/'

# The URL where requests are redirected after login.
# LOGIN_REDIRECT_URL = '/accounts/profile/'


################################################################
# BASE INTERNATIONALIZATION / MISC SETTINGS
################################################################
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
