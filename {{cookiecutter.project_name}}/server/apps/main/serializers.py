from rest_framework import serializers

from server.apps.main.models import BlogPost


class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at',]
