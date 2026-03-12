from dmr.routing import path

from server.apps.main import api
from server.apps.main.views import index

app_name = 'main'

urlpatterns = [
    path('hello/', index, name='hello'),
]

api_routes = [
    path('users/', api.BlogPostCreate.as_view(), name='blog_post_create'),
    path('users/<int:id>', api.BlogPostGet.as_view(), name='blog_post_get'),
]
