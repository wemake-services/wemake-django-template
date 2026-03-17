from __future__ import annotations

from typing import final

import attrs

from server.apps.main.logic.value_objects import BlogPostFullPayload
from server.apps.main.models import BlogPost


@final
@attrs.define(slots=True, frozen=True)
class BlogPostMapper:
    """Preserves all properties of a ``BlogPost``."""

    def __call__(self, blog_post: BlogPost) -> BlogPostFullPayload:
        """Map model to a DTO instance."""
        return BlogPostFullPayload(
            id=blog_post.id,
            title=blog_post.title,
            body=blog_post.body,
        )
