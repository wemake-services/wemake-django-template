from dmr.routing import path

from server.apps.main.api import views

app_name = 'main'

urlpatterns = [
    path('posts/', views.BlogPostCreate.as_view(), name='blog_post_create'),
    path('posts/<int:id>', views.BlogPostGet.as_view(), name='blog_post_get'),
]
