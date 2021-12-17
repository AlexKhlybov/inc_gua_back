from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from django.utils import timezone

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app', backend='redis', broker='redis://{}:6379/1'.format(REDIS_HOST))
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.now = timezone.now

app.conf.beat_schedule = {
    'update_bank_limits': {
        'task': 'bank.tasks.bank_limits.update_bank_limits',
        'schedule': 30.0,
    },
    'update_fz_limits': {
        'task': 'limit.tasks.fz_limits.update_fz_limits',
        'schedule': 30.0,
    },
    'update_principal_limits': {
        'task': 'limit.tasks.principal_limits.update_principal_limits',
        'schedule': 30.0,
    },
    'update_order': {
        'task': 'order.tasks.update_order.update_order',
        'schedule': 60.0,
    },
}
