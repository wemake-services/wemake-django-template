from http import HTTPStatus
from typing import final

import msgspec
import pytest
from django.urls import reverse
from dmr.test import DMRClient
from polyfactory.factories.msgspec_factory import MsgspecFactory

from server.apps.main.infra.dtos import BlogPostCreateDTO, BlogPostDTO
from server.apps.main.models import BlogPost


@final
class _BlogPostCreateFactory(MsgspecFactory[BlogPostCreateDTO]):
    __check_model__ = True


@pytest.mark.django_db
def test_blog_post_create(dmr_client: DMRClient) -> None:
    """Ensures that blog posts can be created."""
    response = dmr_client.post(
        reverse('api:main:blog_post_create'),
        data=msgspec.to_builtins(_BlogPostCreateFactory.build()),
    )

    assert response.status_code == HTTPStatus.CREATED
    blog_post = msgspec.convert(response.json(), type=BlogPostDTO)
    BlogPost.objects.get(pk=blog_post.id)
