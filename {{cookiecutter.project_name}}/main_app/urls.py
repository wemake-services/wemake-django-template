# -*- coding: utf-8 -*-

from django.conf.urls import url

from main_app.views import index

# Place your URLs here:

urlpatterns = [
    url(r'^hello/$', index, name='hello'),
]
