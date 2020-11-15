import django_stubs_ext
from django.contrib import admin

from server.apps.main.models import BlogPost

django_stubs_ext.monkeypatch()


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):  # type: ignore
    """Admin panel example for ``BlogPost`` model."""
