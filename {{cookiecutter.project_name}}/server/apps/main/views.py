import structlog

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from server.apps.main.tasks import test_celery_blogpost


logger = structlog.get_logger(__name__)


def index(request: HttpRequest) -> HttpResponse:
    """
    Main (or index) view.

    Returns rendered default page to the user.
    Typed with the help of ``django-stubs`` project.
    """
    return render(request, 'main/index.html')


def celery_view(request: HttpRequest) -> HttpResponse:
    """
    Main (or index) view.

    Returns rendered default page to the user.
    Typed with the help of ``django-stubs`` project.
    """
    test_celery_blogpost.delay(1)
    return render(request, 'main/index.html')
