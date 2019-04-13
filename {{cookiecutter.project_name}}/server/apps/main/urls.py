# -*- coding: utf-8 -*-

from django.conf.urls import url

from server.apps.main.views import index

# Place your URLs here:

app_name = 'main'

urlpatterns = [
    url(r'^hello/$', index, name='hello'),
]
