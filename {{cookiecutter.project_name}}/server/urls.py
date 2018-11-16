# -*- coding: utf-8 -*-

"""
Main URL mapping configuration file.

Include other URLConfs from external apps using method `include()`.

It is also a good practice to keep a single URL to the root index page.

This examples uses Django's default media
files serving technique in development.
"""

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from server.main_app import urls as main_urls
from server.main_app.views import index

admin.autodiscover()


urlpatterns = [
    # django-admin:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),

    # Apps:
    url(r'^main/', include(main_urls)),

    # Text and xml static files:
    url(r'^robots\.txt$', TemplateView.as_view(
        template_name='txt/robots.txt',
        content_type='text/plain',
    )),
    url(r'^humans\.txt$', TemplateView.as_view(
        template_name='txt/humans.txt',
        content_type='text/plain',
    )),

    # It is a good practice to have explicit index view:
    url(r'^$', index, name='index'),
]

if settings.DEBUG:  # pragma: no cover
    import debug_toolbar  # noqa: Z435
    from django.views.static import serve  # noqa: Z435

    urlpatterns = [
        # URLs specific only to django-debug-toolbar:
        url(r'^__debug__/', include(debug_toolbar.urls)),

        # Serving media files in development only:
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ] + urlpatterns
