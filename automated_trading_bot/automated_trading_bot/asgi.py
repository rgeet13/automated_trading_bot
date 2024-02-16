"""
ASGI config for automated_trading_bot project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from automated_trading_bot.settings.base import DEBUG

from django.core.asgi import get_asgi_application

if DEBUG:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'automated_trading_bot.settings.dev')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'automated_trading_bot.settings.prod')

application = get_asgi_application()
