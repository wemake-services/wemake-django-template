# -*- coding: utf-8 -*-

"""
Main URL mapping configuration file.

Include other URLConfs from external apps using method `include()`.

It is also a good practice to keep a single URL to the root index page.

This examples uses Django's default media
files serving technique in development.
"""

from django.conf import settings
from django.conf.urls import include, path
from django.contrib import admin
from django.contrib.admindocs import urls as admindocs_urls
from django.views.generic import TemplateView
from health_check import urls as health_urls

from server.apps.main import urls as main_urls
from server.apps.main.views import index

admin.autodiscover()


urlpatterns = [
    # Apps:
    path('^main/', include(main_urls, namespace='main')),

    # Health checks:
    path(r'^health/', include(health_urls)),  # noqa: DJ05

    # django-admin:
    path('^admin/doc/', include(admindocs_urls)),  # noqa: DJ05
    path('^admin/', admin.site.urls),

    # Text and xml static files:
    path('^robots\.txt$', TemplateView.as_view(
        template_name='txt/robots.txt',
        content_type='text/plain',
    )),
    path('^humans\.txt$', TemplateView.as_view(
        template_name='txt/humans.txt',
        content_type='text/plain',
    )),

    # It is a good practice to have explicit index view:
    path(r'^$', index, name='index'),
]

if settings.DEBUG:  # pragma: no cover
    import debug_toolbar  # noqa: Z435
    from django.views.static import serve  # noqa: Z435

    urlpatterns = [
        # URLs specific only to django-debug-toolbar:
        path('^__debug__/', include(debug_toolbar.urls)),  # noqa: DJ05

        # Serving media files in development only:
        path('^media/(<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ] + urlpatterns
