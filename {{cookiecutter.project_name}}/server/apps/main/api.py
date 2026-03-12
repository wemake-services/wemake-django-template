from http import HTTPStatus
from typing import final

from dmr import (
    APIError,
    Body,
    Controller,
    Path,
)
from dmr.plugins.msgspec import MsgspecSerializer

from server.apps.main.infra.dtos import BlogPostCreateDTO, BlogPostDTO
from server.apps.main.logic.usecases import blogpost_create, blogpost_get
from server.common.di import HasContainer
from server.common.dtos import IntIdPath

# NOTE: there are no tests for the API. But, coverage is 100%
# Thanks to the `schemathesis`!


@final
class BlogPostCreate(
    Body[BlogPostCreateDTO],
    Controller[MsgspecSerializer],
    HasContainer,
):
    """Top level endpoints for the ``BlogPost`` model."""

    def post(self) -> BlogPostDTO:
        """Create new ``BlogPost`` model."""
        return self._resolve(blogpost_create.CreateBlogPost)(self.parsed_body)


@final
class BlogPostGet(
    Path[IntIdPath],
    Controller[MsgspecSerializer],
    HasContainer,
):
    """Endpoints that only require a path for ``BlogPost`` models."""

    def get(self) -> BlogPostDTO:
        """Return existing ``BlogPost`` model by id."""
        blog_post = self._resolve(blogpost_get.GetBlogPost)(self.parsed_path.id)
        if blog_post is None:
            raise APIError(
                self.format_error('Blog post not found'),
                status_code=HTTPStatus.NOT_FOUND,
            )
        return blog_post
