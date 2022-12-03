from http import HTTPStatus

from django.test import Client
from django.urls import reverse


def test_main_page(client: Client, main_heading: str) -> None:
    """This test ensures that main page works."""
    response = client.get(reverse('index'))

    assert response.status_code == HTTPStatus.OK
    assert main_heading in str(response.content)


def test_hello_page(client: Client, main_heading: str) -> None:
    """This test ensures that hello page works."""
    response = client.get(reverse('main:hello'))

    assert response.status_code == HTTPStatus.OK
    assert main_heading in str(response.content)
