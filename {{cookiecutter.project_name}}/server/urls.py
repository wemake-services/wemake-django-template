# -*- coding: utf-8 -*-

"""
Main URL mapping configuration file.

Include other URLConfs from external apps using method include().

It is also a good practice to keep a single URL to the root index page.

This examples uses Django's default media
files serving technique in development.
"""

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from main_app import urls as main_urls
from main_app.views import index

admin.autodiscover()


urlpatterns = [
    # django-admin:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

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
    url(r'^crossdomain\.xml$', TemplateView.as_view(
        template_name='txt/crossdomain.xml',
        content_type='application/xml',
    )),

    # It is a good practice to have explicit index view:
    url(r'^$', index, name='index'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

# Customize default error views:
# https://docs.djangoproject.com/en/1.11/topics/http/views/#customizing-error-views

# handler400 = 'your_app.views.error_handler'
# handler403 = 'your_app.views.error_handler'
# handler404 = 'your_app.views.error_handler'
# handler500 = 'your_app.views.error_handler'
