from __future__ import annotations

from typing import TYPE_CHECKING, final

import attrs

from server.apps.main.logic.value_objects import BlogPostFullPayload

if TYPE_CHECKING:
    from server.apps.main.infra import mappers, repository


@final
@attrs.define(slots=True, frozen=True)
class GetBlogPost:
    """Get ``BlogPost`` models by primary key."""

    _repository: repository.BlogPostRepo
    _mapper: mappers.BlogPostMapper

    def __call__(self, blog_post_id: int) -> BlogPostFullPayload:
        """
        There's no real story to tell about this example.

        But here you need to put a text description of what business
        needs to be done in this usecase.
        """
        return self._mapper(self._repository.get_by_id(blog_post_id))
