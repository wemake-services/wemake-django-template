from http import HTTPStatus
from typing import final, override

from django.http import HttpResponse
from dmr import Body, Controller, modify
from dmr.endpoint import Endpoint
from dmr.errors import ErrorType
from dmr.metadata import ResponseSpec
from dmr.openapi.objects import Link
from dmr.plugins.msgspec import MsgspecSerializer

from server.apps.main.logic.usecases import blogpost_create, blogpost_get
from server.apps.main.logic.value_objects import (
    BlogPostCreatePayload,
    BlogPostFullPayload,
)
from server.apps.main.models import BlogPost
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
        return self._resolve(blogpost_create.CreateBlogPost)(self.parsed_body)


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
        return self._resolve(blogpost_get.GetBlogPost)(self.kwargs['id'])

    @override
    def handle_error(
        self,
        endpoint: Endpoint,
        controller: Controller[MsgspecSerializer],
        exc: Exception,
    ) -> HttpResponse:
        """Handle specific errors for this controller."""
        if isinstance(exc, BlogPost.DoesNotExist):
            return self.to_error(
                self.format_error(
                    'Blog post not found',
                    error_type=ErrorType.not_found,
                ),
                status_code=HTTPStatus.NOT_FOUND,
            )
        return super().handle_error(endpoint, controller, exc)
