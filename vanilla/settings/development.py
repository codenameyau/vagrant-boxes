"""
Django settings for local development.

If each developer needs their own development settings file,
then feel free to add this file to .gitignore
"""
from vanilla.settings.base import *

################################################################
# BASE APPLICATION SETTINGS
################################################################
INSTALLED_APPS += [

]


################################################################
# LOCAL CONFIGURATION SETTINGS
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

# Use local memchaced instance
CACHES = {
   'default': {
       'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
       'LOCATION': 'localhost:11211'
   },
}
