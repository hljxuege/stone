from django.conf.urls import patterns, include, url

import users
import store
import captcha
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'stone.views.home', name='home'),
    # url(r'^stone/', include('stone.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^users/', include('users.urls')),
    # url(r'^store/', include('store.urls')),
)

urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)