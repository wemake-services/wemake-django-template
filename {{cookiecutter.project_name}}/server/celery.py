import os
import sys

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
PROJECT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
APPS_PATH = os.path.abspath(os.path.join(PROJECT_PATH, "server", "apps"))


if APPS_PATH not in sys.path:
    sys.path.insert(0, APPS_PATH)

app = Celery('server')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


'''
Task for testing
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
'''
