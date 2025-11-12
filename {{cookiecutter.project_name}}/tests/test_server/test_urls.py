from http import HTTPStatus
from typing import Final

import pytest
from django.test import Client
from django.urls import reverse

_HEALTH_URL: Final = reverse('health_check:health_check_home')
_ADMIN_URL: Final = reverse('admin:index')
_ADMIN_DOC_URL: Final = reverse('django-admindocs-docroot')
_ROBOTS_URL: Final = reverse('robots_txt')
_HUMANS_URL: Final = reverse('humans_txt')


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
