from django.conf.urls import patterns, url

urlpatterns = patterns(
    'profile.views',
    # url(r'profile/$', 'user_profile'),
    url(r'login/$', 'login'),
    url(r'auth/$', 'auth_view'),
    url(r'logout/$', 'logout', name='logout'),
    url(r'logged_in/$', 'logged_in'),
    url(r'invalid/$', 'invalid_login'),
    # url(r'register/$', 'register_user'),
    # url(r'register_success/$', 'register_success'),
    url(r'profile/$', 'profile', name='profile'),
)
