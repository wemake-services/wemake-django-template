# -*- coding: utf-8 -*-

from django.conf.urls import url

from main_app.views import hello

# Place your URLs here:

urlpatterns = [
    url(r'^hello/$', hello, name='hello'),
]
