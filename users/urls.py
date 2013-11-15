from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('users',
    # Examples:
    url(r'^$', 'views.sign_in', name='sign'),
    url(r'^sign/$', 'views.sign_in', name='sign2'),
    url(r'^sign_out/$', 'views.sign_out', name='sign-out'),
    url(r'^get_user_profile/$', 'views.get_user_profile', name='user-profile'),
    url(r'^create_user/$', 'views.create_user', name='create-user'),
    url(r'^get_login_user/$', 'views.get_login_user', name='get-login-user'),
	url(r'^show_user_info/(?P<user_id>\d+)/$', 'views.show_user_info', name='show-user-info'),
	url(r'^list_users/$', 'views.list_users', name='list-users'),
	url(r'^ajax_get_user_info_by_usercode/$', 'views.ajax_get_user_info_by_usercode', name='ajax-get-user-info-by-usercode'),
	
)

