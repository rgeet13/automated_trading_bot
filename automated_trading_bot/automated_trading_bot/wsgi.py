"""
WSGI config for automated_trading_bot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from automated_trading_bot.settings.base import DEBUG

from django.core.wsgi import get_wsgi_application
if DEBUG:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'automated_trading_bot.settings.dev')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'automated_trading_bot.settings.prod')

application = get_wsgi_application()
