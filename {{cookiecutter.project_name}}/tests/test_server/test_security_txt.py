import datetime as dt
from typing import Final

from django.test import Client
from django.urls import reverse

_SECURITY_URL: Final = reverse('security_txt')


def test_security_txt_contact(client: Client) -> None:
    """Ensures that security contact information is present."""
    response = client.get(_SECURITY_URL)

    contacts = [
        line.removeprefix('Contact: ').strip()
        for line in response.text.splitlines()
        if line.startswith('Contact: ')
    ]

    assert contacts
    assert all(contacts)


def test_security_txt_expires(client: Client) -> None:
    """Ensures that security contact information has not expired."""
    response = client.get(_SECURITY_URL)

    expiry_dates = [
        line.removeprefix('Expires: ')
        for line in response.text.splitlines()
        if line.startswith('Expires: ')
    ]

    assert len(expiry_dates) == 1
    expires = dt.datetime.fromisoformat(expiry_dates[0])
    assert expires.tzinfo is not None
    assert expires > dt.datetime.now(dt.UTC)
