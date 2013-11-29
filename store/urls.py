from django.conf.urls import patterns, include, url

urlpatterns = patterns('store',
    url(r'^$', 'views.home', name='random-goods'),
    url(r'^goods_list/$', 'views.goods_list', name='goods-list'),
)
