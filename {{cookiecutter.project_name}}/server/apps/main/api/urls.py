from dmr.routing import path

from server.apps.main.api import views

app_name = 'main'

urlpatterns = [
    path('users/', views.BlogPostCreate.as_view(), name='blog_post_create'),
    path('users/<int:id>', views.BlogPostGet.as_view(), name='blog_post_get'),
]
