from django.conf.urls import patterns, include, url

urlpatterns = patterns('store',
    url(r'^$', 'views.home'),
)
