from dmr.routing import Router, path

from server.apps.main import api
from server.apps.main.views import index

app_name = 'main'

urlpatterns = [
    path('hello/', index, name='hello'),
]

router = Router(
    'users/',
    [
        path('', api.BlogPostCreate.as_view(), name='blog_post_create'),
        path('<int:id>/', api.BlogPostGet.as_view(), name='blog_post_get'),
    ],
)
