from http import HTTPStatus
from typing import final

from dmr import (
    APIError,
    Body,
    Controller,
    modify,
)
from dmr.errors import ErrorType
from dmr.metadata import ResponseSpec
from dmr.openapi.objects import Link
from dmr.plugins.msgspec import MsgspecSerializer

from server.apps.main.logic.usecases import blogpost_create, blogpost_get
from server.apps.main.logic.value_objects import (
    BlogPostCreatePayload,
    BlogPostFullPayload,
)
from server.common.di import HasContainer


@final
class BlogPostCreate(
    Body[BlogPostCreatePayload],
    Controller[MsgspecSerializer],
    HasContainer,
):
    """Top level endpoints for the ``BlogPost`` model."""

    @modify(
        # This is only needed as a schemathesis demo:
        # https://schemathesis.readthedocs.io/en/stable/guides/stateful-testing
        links={
            'GetBlogPostById': Link(
                operation_id='getBlogPostGetApiUserUsers',
                parameters={'id': '$response.body#/id'},
            ),
        },
    )
    def post(self) -> BlogPostFullPayload:
        """Create new ``BlogPost`` model."""
        blog_post = self._resolve(blogpost_create.CreateBlogPost)(
            self.parsed_body,
        )
        if blog_post is None:
            raise APIError(
                self.format_error('Wrong blog post'),
                status_code=HTTPStatus.BAD_REQUEST,
            )
        return blog_post


@final
class BlogPostGet(
    Controller[MsgspecSerializer],
    HasContainer,
):
    """Endpoints that only require a path for ``BlogPost`` models."""

    responses = (
        ResponseSpec(Controller.error_model, status_code=HTTPStatus.NOT_FOUND),
    )

    def get(self) -> BlogPostFullPayload:
        """Return existing ``BlogPost`` model by id."""
        blog_post = self._resolve(blogpost_get.GetBlogPost)(self.kwargs['id'])
        if blog_post is None:
            raise APIError(
                self.format_error(
                    'Blog post not found',
                    error_type=ErrorType.not_found,
                ),
                status_code=HTTPStatus.NOT_FOUND,
            )
        return blog_post
