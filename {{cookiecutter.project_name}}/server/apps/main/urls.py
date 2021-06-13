from django.urls import path

from server.apps.main.views import index

app_name = 'main'

urlpatterns = [
    path('hello/', index, name='hello'),
]
