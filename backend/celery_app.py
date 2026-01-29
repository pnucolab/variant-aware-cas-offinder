"""Celery application configuration with periodic task scheduling."""
import os

from celery import Celery
from celery.schedules import crontab

celery_task = Celery(
    'app',
    broker=os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/0"),
    backend=os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379/0"),
    include=['celery_worker']
)

# Celery configuration
celery_task.conf.update(
    timezone='UTC',
    broker_connection_retry_on_startup=True,
    beat_schedule={
        'cleanup-old-results-daily': {
            'task': 'celery_worker.cleanup_old_results',
            'schedule': crontab(hour=2, minute=0),  
        },
    },
)