from http import HTTPStatus
from typing import Final

import pytest
from django.test import Client
from django.urls import reverse

_OPENAPI_URLS: Final = (
    reverse('openapi_json'),
    reverse('openapi_yaml'),
    reverse('stoplight'),
    reverse('swagger'),
    reverse('scalar'),
    reverse('redoc'),
)


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
