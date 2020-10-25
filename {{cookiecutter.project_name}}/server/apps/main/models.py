import textwrap
from typing import Final, final

from django.db import models

#: That's how constants should be defined.
_POST_TITLE_MAX_LENGTH: Final = 80


@final
class BlogPost(models.Model):
    """
    This model is used just as an example.

    With it we show how one can:
    - Use fixtures and factories
    - Use migrations testing

    """

    title = models.CharField(max_length=_POST_TITLE_MAX_LENGTH)
    body = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(object):
        verbose_name = 'BlogPost'  # You can probably use `gettext` for this
        verbose_name_plural = 'BlogPosts'

    def __str__(self) -> str:
        """All django models should have this method."""
        return textwrap.wrap(self.title, _POST_TITLE_MAX_LENGTH // 4)[0]
