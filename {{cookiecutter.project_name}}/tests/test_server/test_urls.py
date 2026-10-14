from http import HTTPStatus
from typing import Final

import pytest
from django.test import Client
from django.urls import reverse

_HEALTH_URL: Final = reverse('health_check')
_ADMIN_URL: Final = reverse('admin:index')
_ADMIN_DOC_URL: Final = reverse('django-admindocs-docroot')
_ROBOTS_URL: Final = reverse('robots_txt')
_HUMANS_URL: Final = reverse('humans_txt')
_OPENAPI_URLS: Final = frozenset((
    reverse('openapi_json'),
    reverse('openapi_yaml'),
    reverse('stoplight'),
    reverse('swagger'),
    reverse('scalar'),
    reverse('redoc'),
))


@pytest.mark.django_db
def test_health_check(client: Client) -> None:
    """Ensures that health check is accessible."""
    response = client.get(_HEALTH_URL)

    assert response.status_code == HTTPStatus.OK


def test_admin_unauthorized(client: Client) -> None:
    """Ensures that admin panel requires auth."""
    response = client.get(_ADMIN_URL)

    assert response.status_code == HTTPStatus.FOUND


def test_admin_authorized(admin_client: Client) -> None:
    """Ensures that admin panel is accessible."""
    response = admin_client.get(_ADMIN_URL)

    assert response.status_code == HTTPStatus.OK


def test_admin_docs_unauthorized(client: Client) -> None:
    """Ensures that admin panel docs requires auth."""
    response = client.get(_ADMIN_DOC_URL)

    assert response.status_code == HTTPStatus.FOUND


def test_admin_docs_authorized(admin_client: Client) -> None:
    """Ensures that admin panel docs are accessible."""
    response = admin_client.get(_ADMIN_DOC_URL)

    assert response.status_code == HTTPStatus.OK
    assert b'docutils' not in response.content


@pytest.mark.parametrize('page', _OPENAPI_URLS)
def test_openapi_unauthorized(client: Client, *, page: str) -> None:
    """Ensures that OpenAPI resources require staff authentication."""
    response = client.get(page)

    assert response.status_code == HTTPStatus.FOUND


@pytest.mark.parametrize('page', _OPENAPI_URLS)
def test_openapi_authorized(admin_client: Client, *, page: str) -> None:
    """Ensures that OpenAPI resources are accessible to staff."""
    response = admin_client.get(page)

    assert response.status_code == HTTPStatus.OK


@pytest.mark.parametrize(
    'page',
    [
        _ROBOTS_URL,
        _HUMANS_URL,
    ],
)
def test_specials_txt(client: Client, page: str) -> None:
    """Ensures that special `txt` files are accessible."""
    response = client.get(page)

    assert response.status_code == HTTPStatus.OK
    assert response.get('Content-Type') == 'text/plain'
