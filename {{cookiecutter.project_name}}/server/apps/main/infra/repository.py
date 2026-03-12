from __future__ import annotations

from typing import final

import attrs

from server.apps.main.infra.dtos import BlogPostCreateDTO
from server.apps.main.models import BlogPost


@final
@attrs.define(slots=True, frozen=True)
class BlogPostRepo:
    """Repository for the ``BlogPost`` model."""

    def create(self, parsed_body: BlogPostCreateDTO) -> BlogPost:
        """Creates new ``BlogPost`` model."""
        # TODO: technically this is not correct, because creation can fail:
        return BlogPost.objects.create(
            title=parsed_body.title,
            body=parsed_body.body,
        )

    def get_or_none(self, blog_post_id: int) -> BlogPost | None:
        """Return ``BlogPost`` model by the primary key."""
        return BlogPost.objects.filter(pk=blog_post_id).first()
