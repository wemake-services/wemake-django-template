# -*- coding: utf-8 -*-

from django.conf.urls import url

from server.main_app.views import index

# Place your URLs here:

app_name = 'main_app'

urlpatterns = [
    url(r'^hello/$', index, name='hello'),
]
