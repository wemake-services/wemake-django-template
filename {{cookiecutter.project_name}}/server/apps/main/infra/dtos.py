from typing import Annotated, final

import msgspec

from server.apps.main.logic.constants import POST_TITLE_MAX_LENGTH


class BlogPostCreateDTO(msgspec.Struct):
    """Used to create ``BlogPost`` models."""

    title: Annotated[
        str, msgspec.Meta(min_length=1, max_length=POST_TITLE_MAX_LENGTH)
    ]
    body: str


@final
class BlogPostDTO(BlogPostCreateDTO):
    """Used to represent existing ``BlogPost`` models."""

    id: int
