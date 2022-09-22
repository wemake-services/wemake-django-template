from rest_framework import viewsets

from server.apps.main.models import BlogPost
from server.apps.main.serializers import BlogPostSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
