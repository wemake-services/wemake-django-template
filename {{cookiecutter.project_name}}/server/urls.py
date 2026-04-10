"""
Main URL mapping configuration file.

Include other URLConfs from external apps using method `include()`.

It is also a good practice to keep a single URL to the root index page.

This examples uses Django's default media
files serving technique in development.
"""

from django.conf import settings
from django.contrib import admin
from django.contrib.admindocs import urls as admindocs_urls
from django.urls import include
from django.views.generic import TemplateView
from dmr.openapi import build_schema
from dmr.openapi.views import (
    OpenAPIJsonView,
    RedocView,
    ScalarView,
    StoplightView,
    SwaggerView,
)
from dmr.openapi.views.yaml import OpenAPIYamlView
from dmr.plugins.msgspec import MsgspecSerializer
from dmr.routing import Router, build_404_handler, build_500_handler, path
from health_check.views import HealthCheckView

from server.apps.main import urls as main_urls
from server.apps.main.api import urls as main_api_urls
from server.apps.main.views import index

admin.autodiscover()

router = Router(
    'api/',
    [
        path('user/', include(main_api_urls, namespace='main')),
    ],
)
schema = build_schema(router)

handler404 = build_404_handler(router.prefix, serializer=MsgspecSerializer)
handler500 = build_500_handler(router.prefix, serializer=MsgspecSerializer)

urlpatterns = [
    # Apps:
    path('main/', include(main_urls, namespace='main')),
    # Apis:
    path(router.prefix, include((router.urls, 'server'), namespace='api')),
    # OpenAPI:
    path(
        'docs/openapi.json/',
        OpenAPIJsonView.as_view(schema),
        name='openapi_json',
    ),
    path(
        'docs/openapi.yaml/',
        OpenAPIYamlView.as_view(schema),
        name='openapi_yaml',
    ),
    path('docs/stoplight/', StoplightView.as_view(schema), name='stoplight'),
    path('docs/swagger/', SwaggerView.as_view(schema), name='swagger'),
    path('docs/scalar/', ScalarView.as_view(schema), name='scalar'),
    path('docs/redoc/', RedocView.as_view(schema), name='redoc'),
    # Health checks:
    path(
        'health/',
        HealthCheckView.as_view(
            checks=[
                'health_check.Cache',
                'health_check.Database',
                'health_check.Storage',
            ],
        ),
        name='health_check',
    ),
    # django-admin:
    path('admin/doc/', include(admindocs_urls)),
    path('admin/', admin.site.urls),
    # Text and xml static files:
    path(
        'robots.txt',
        TemplateView.as_view(
            template_name='common/txt/robots.txt',
            content_type='text/plain',
        ),
        name='robots_txt',
    ),
    path(
        'humans.txt',
        TemplateView.as_view(
            template_name='common/txt/humans.txt',
            content_type='text/plain',
        ),
        name='humans_txt',
    ),
    # It is a good practice to have explicit index view:
    path('', index, name='index'),
]

if settings.DEBUG:  # pragma: no cover
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns = [
        # URLs specific only to django-debug-toolbar:
        path('__debug__/', include(debug_toolbar.urls)),
        *urlpatterns,
        # Serving media files in development only:
        *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    ]
