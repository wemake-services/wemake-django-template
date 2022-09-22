from django.urls import path

from server.apps.main.views import index, celery_view

app_name = 'main'

urlpatterns = [
    path('hello/', index, name='hello'),
    path('celery/', celery_view, name='celery_view'),
]
