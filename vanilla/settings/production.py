"""
Django settings for production.

Deploying static files in Production:
https://docs.djangoproject.com/en/1.7/howto/static-files/deployment/

Configuring your cache settings:
https://docs.djangoproject.com/en/1.7/ref/settings/#caches

Memcached with Heroku:
https://devcenter.heroku.com/articles/django-memcache
"""
from vanilla.settings.base import *

################################################################
# PRODUCTION CONFIGURATION SETTINGS
################################################################

# Deployment hosts
ALLOWED_HOSTS += [
]

# For larger sites, it is recommended to host
# static and media files on different servers.


################################################################
# PRODUCTION CACHE SETTINGS
################################################################
CACHE_MIDDLEWARE_SECONDS = 300
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': [
            '127.0.0.1:11211'
        ],
        'TIMEOUT': 300,
    }
}


################################################################
# PRODUCTION LOGGING SETTINGS
################################################################
