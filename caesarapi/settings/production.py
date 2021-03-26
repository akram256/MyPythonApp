import sentry_sdk
from .base import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.redis import RedisIntegration
from sentry_sdk.integrations.celery import CeleryIntegration
import logging



sentry_sdk.init(
    dsn="https://88c53707d20c4c8690bfe1f630bfd978@sentry.io/1536312",
    integrations=[
        DjangoIntegration(),
        RedisIntegration(),
        CeleryIntegration()
    ]
)

DEBUG=True

ALLOWED_HOSTS =['*']

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
USE_X_FORWARDED_HOST = True

