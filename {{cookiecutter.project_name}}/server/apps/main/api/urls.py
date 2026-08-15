from dmr.routing import Router, path

from server.apps.main.api import views

router = Router(
    'user/',
    [
        path('posts/', views.BlogPostCreate.as_view(), name='blog_post_create'),
        path(
            'posts/<int:id>',
            views.BlogPostGet.as_view(),
            name='blog_post_get',
        ),
    ],
)
