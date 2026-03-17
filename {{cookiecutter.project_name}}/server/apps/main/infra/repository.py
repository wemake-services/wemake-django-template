from __future__ import annotations

from typing import final

import attrs

from server.apps.main.logic.value_objects import BlogPostCreatePayload
from server.apps.main.models import BlogPost


@final
@attrs.define(slots=True, frozen=True)
class BlogPostRepo:
    """Repository for the ``BlogPost`` model."""

    def create(self, parsed_body: BlogPostCreatePayload) -> BlogPost | None:
        """Creates new ``BlogPost`` model."""
        try:
            return BlogPost.objects.create(
                title=parsed_body.title,
                body=parsed_body.body,
            )
        except Exception:
            return None

    def get_or_none(self, blog_post_id: int) -> BlogPost | None:
        """Return ``BlogPost`` model by the primary key."""
        return BlogPost.objects.filter(pk=blog_post_id).first()
