import structlog
from celery import shared_task

from server.apps.main.models import BlogPost


logger = structlog.get_logger(__name__)


@shared_task
def test_celery_blogpost(post_id):
    try:
        blog_post = BlogPost.objects.get(id=post_id)
        logger.info('Found blog post', blog_post=blog_post)
    except BlogPost.DoesNotExist:
        logger.info('Blog post does not exist', blog_post=post_id)
