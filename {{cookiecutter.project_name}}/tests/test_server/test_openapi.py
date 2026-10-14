from http import HTTPStatus
from typing import Final

import pytest
from django.test import Client
from django.urls import reverse

_OPENAPI_URLS: Final = (
    reverse('v1_openapi_json'),
    reverse('v1_openapi_yaml'),
    reverse('v1_stoplight'),
    reverse('v1_swagger'),
    reverse('v1_scalar'),
    reverse('v1_redoc'),
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
