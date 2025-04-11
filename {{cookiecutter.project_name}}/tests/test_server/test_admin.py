from http import HTTPStatus

import pytest
from django.contrib.admin import AdminSite, ModelAdmin
from django.contrib.admin.sites import all_sites
from django.db.models import Model
from django.test import Client
from django.urls import reverse

_MODEL_ADMIN_PARAMS = [
    (site, model, model_admin)
    for site in all_sites
    for model, model_admin in site._registry.items()  # noqa: SLF001
]


def _make_url(site, model: type[Model], page: str) -> str:
    """Generates a URL for the given admin site, model, and page."""
    return reverse(
        f'{site.name}:{model._meta.app_label}_{model._meta.model_name}_{page}'  # noqa: SLF001
    )


@pytest.mark.django_db
@pytest.mark.parametrize(
    ('site', 'model', 'model_admin'),
    _MODEL_ADMIN_PARAMS,
)
def test_admin_changelist(
    admin_client: Client,
    site: AdminSite,
    model: type[Model],
    model_admin: type[ModelAdmin],
) -> None:
    """This test ensures that admin changelist pages are accessible."""
    url = _make_url(site, model, 'changelist')
    response = admin_client.get(url, {'q': 'something'})

    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
@pytest.mark.parametrize(
    ('site', 'model', 'model_admin'),
    _MODEL_ADMIN_PARAMS,
)
def test_admin_add(
    admin_client: Client,
    site: AdminSite,
    model: type[Model],
    model_admin: type[ModelAdmin],
) -> None:
    """This test ensures that admin add pages are accessible or restricted."""
    url = _make_url(site, model, 'add')
    response = admin_client.get(url)

    assert response.status_code in {HTTPStatus.OK, HTTPStatus.FORBIDDEN}
