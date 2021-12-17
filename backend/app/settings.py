from garpixcms.settings import *  # noqa
from garpixcms.settings import INSTALLED_APPS, MIDDLEWARE
import os
from .basedir import BASE_DIR

INSTALLED_APPS += [
    'django_filters',
    'content',
    'order',
    'bank',
    'limit',
    'handbook',
    'entity',
    'changelog',
    'config',
    'api',
    'django_fsm',
    'django_fsm_log',
    'drf_yasg',
]

MIDDLEWARE += [
    'changelog.middleware.LoggedInUserMiddleware',
]

# notify
SITE_URL = os.getenv('SITE_URL', '')
AUTH_USER_MODEL = 'user.User'
NOTIFY_EVENT_RESTORE_PASSWORD = 1
NOTIFY_EVENTS = {
    NOTIFY_EVENT_RESTORE_PASSWORD: {
        'title': 'сброс / восстановление пароля',
        'context_description': '{{ password_reset_key }} - ключ смены пароля',  # noqa
        'event_description': 'Смена пароля',
    },
}

CHOICES_NOTIFY_EVENT = [(k, v['title']) for k, v in NOTIFY_EVENTS.items()]
NOTIFY_HELP_TEXT = """
    <h3>Переменные в письме</h3>
"""

NOTIFY_SMS_URL = "http://sms.ru/sms/send"

NOTIFY_SMS_API_ID = "1234567890"

FCM_DJANGO_SETTINGS = {
    "FCM_SERVER_KEY": "1234567890"
}

SEND_SMS = False

LANGUAGE_CODE = 'ru-RU'
USE_I18N = True
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

CELERY_BEAT_SCHEDULE = {
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
        'schedule': os.getenv('SCHEDULE_RETRY_TIME', 60),
    },
}
