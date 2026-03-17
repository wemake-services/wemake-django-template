from __future__ import annotations

from typing import TYPE_CHECKING, final

import attrs

from server.apps.main.logic.value_objects import (
    BlogPostCreatePayload,
    BlogPostFullPayload,
)

if TYPE_CHECKING:
    from server.apps.main.infra import mappers, repository


@final
@attrs.define(slots=True, frozen=True)
class CreateBlogPost:
    """Creates ``BlogPost`` instances."""

    _repository: repository.BlogPostRepo
    _mapper: mappers.BlogPostMapper

    def __call__(
        self,
        parsed_body: BlogPostCreatePayload,
    ) -> BlogPostFullPayload | None:
        """
        There's no real story to tell about this example.

        But here you need to put a text description of what business
        needs to be done in this usecase.
        """
        blog_post = self._repository.create(parsed_body)
        if blog_post is None:
            return blog_post
        return self._mapper(blog_post)
