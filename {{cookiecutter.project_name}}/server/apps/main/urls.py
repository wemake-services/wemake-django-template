# -*- coding: utf-8 -*-

from django.urls import path

from server.apps.main.views import index

# Place your URLs here:

app_name = 'main'

urlpatterns = [
    path('hello', index, name='hello'),
]
