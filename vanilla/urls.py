from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    # Grappelli jazzy admin skin
    url(r'^grappelli/', include('grappelli.urls')),

    # Obscure the admin URL with a long random string.
    url(r'^django-admin/', include(admin.site.urls)),

    # Examples:
    # url(r'^$', 'vanilla.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
)
