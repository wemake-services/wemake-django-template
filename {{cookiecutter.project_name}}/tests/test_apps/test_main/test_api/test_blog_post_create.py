from http import HTTPStatus
from typing import final

import msgspec
import pytest
from django.urls import reverse
from dmr.test import DMRClient
from inline_snapshot import snapshot
from inline_snapshot_django import snapshot_queries
from polyfactory.factories.msgspec_factory import MsgspecFactory

from server.apps.main.logic.value_objects import (
    BlogPostCreatePayload,
    BlogPostFullPayload,
)
from server.apps.main.models import BlogPost


@final
class _BlogPostCreateFactory(MsgspecFactory[BlogPostCreatePayload]):
    __check_model__ = True


@pytest.mark.django_db
def test_blog_post_create(dmr_client: DMRClient) -> None:
    """Ensures that blog posts can be created."""
    with snapshot_queries() as snap:
        response = dmr_client.post(
            reverse('api:main:blog_post_create'),
            data=msgspec.to_builtins(_BlogPostCreateFactory.build()),
        )

    assert response.status_code == HTTPStatus.CREATED
    assert snap == snapshot([
        'INSERT INTO main_blogpost (...) VALUES (...) RETURNING ...',
    ])
    blog_post = msgspec.convert(response.json(), type=BlogPostFullPayload)
    BlogPost.objects.get(pk=blog_post.id)
