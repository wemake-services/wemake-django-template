from http import HTTPStatus

import msgspec
import pytest
from django.urls import reverse
from dmr.test import DMRClient
from faker import Faker

from server.apps.main.logic.value_objects import BlogPostFullPayload
from server.apps.main.models import BlogPost


@pytest.fixture
def blog_post(faker: Faker) -> BlogPost:
    """Generate fake ``BlogPost`` instance."""
    # TODO: this should be done with a model generator like
    # https://github.com/fcurella/django-fakery
    return BlogPost.objects.create(
        title=faker.name(),
        body=faker.text(),
    )


@pytest.mark.django_db
def test_blog_post_get(dmr_client: DMRClient, blog_post: BlogPost) -> None:
    """Ensures that blog posts can be fetched."""
    response = dmr_client.get(
        reverse('api:main:blog_post_get', kwargs={'id': blog_post.pk}),
    )

    assert response.status_code == HTTPStatus.OK
    msgspec.convert(response.json(), type=BlogPostFullPayload)


@pytest.mark.django_db
def test_blog_post_get_missing(dmr_client: DMRClient) -> None:
    """Ensures that blog posts can be fetched."""
    response = dmr_client.get(
        reverse('api:main:blog_post_get', kwargs={'id': 0}),
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        'detail': [{'msg': 'Blog post not found', 'type': 'not_found'}],
    }
