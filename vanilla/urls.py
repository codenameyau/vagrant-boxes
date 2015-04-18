from django.conf.urls import patterns, include, url
from django.contrib import admin
from vanilla.apps.website import views as website

urlpatterns = patterns('',

    # Grappelli jazzy admin skin
    url(r'^grappelli/', include('grappelli.urls')),

    # Obscure the admin URL with a long random string.
    url(r'^django-admin/', include(admin.site.urls)),

    # Home page URL:
    url(r'^$', website.home, name='homepage'),
)
