import textwrap
from typing import final, override

from django.db import models

from server.apps.main.logic.constants import POST_TITLE_MAX_LENGTH


@final
class BlogPost(models.Model):
    """
    This model is used just as an example.

    With it we show how one can:
    - Use fixtures and factories
    - Use migrations testing
    """

    title = models.CharField(max_length=POST_TITLE_MAX_LENGTH)
    body = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # You can use `gettext` to translate model names:
        verbose_name = 'BlogPost'
        verbose_name_plural = 'BlogPosts'

    @override
    def __str__(self) -> str:
        """All django models should have this method."""
        return textwrap.wrap(self.title, POST_TITLE_MAX_LENGTH // 4)[0]
