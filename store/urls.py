from django.conf.urls import patterns, include, url

urlpatterns = patterns('store',
    url(r'^$', 'views.home', name='random-goods'),
    url(r'^goods_list/$', 'views.goods_list', name='goods-list'),
    url(r'^good_type_list/$', 'views.good_type_list', name='good-type-list'),
    url(r'^good_detail/(?P<good_type>\s+)/(?P<good_id>\d+)/$', 'views.good_detail', name='good-detail'),
	url(r'^good_of_goodtypes/(?P<goodtype_id>\d+)/$', 'views.good_of_goodtypes', name='good-of-goodtypes'),
    
)
