from celery import Celery
import os

redis_url = os.getenv("REDIS_URL", "redis://redis:6379/0")

celery_app = Celery(__name__, broker=redis_url, backend=redis_url)

celery_app.conf.beat_schedule = {
    'fill-bucket-every-minute': {
        'task': 'celery_tasks.tasks.fill_bucket',
        'schedule': 60.0,  # Run every minute
    },
}
celery_app.conf.timezone = 'UTC'
celery_app.autodiscover_tasks(packages=['celery_tasks'], force=True)