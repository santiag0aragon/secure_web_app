from django.conf.urls import patterns, url
from messages_app.views import show_notification, delete_notification, main

urlpatterns = patterns(
    "messages_app.views",
    url(r'^show/(?P<notification_id>\d+)/$', show_notification),
    url(r'^delete/(?P<notification_id>\d+)/$', delete_notification),
    url(r'^main/$', main),
)
