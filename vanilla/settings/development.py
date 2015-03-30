"""
Django settings for local development.

If each developer needs their own development settings file,
then feel free to add this file to .gitignore
"""
from vanilla.settings.base import *

################################################################
# DEVELOPMENT APPLICATION SETTINGS
################################################################
INSTALLED_APPS += [

]


################################################################
# DEVELOPMENT CONFIGURATION SETTINGS
################################################################
DEBUG = True
TEMPLATE_DEBUG = True

# Force templates to reload on refresh
TEMPLATE_LOADERS = (
    (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )
)


################################################################
# DEVELOPMENT CACHE SETTINGS
################################################################
CACHE_MIDDLEWARE_SECONDS = 30
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 30,
    }
}
