from django.db import models

class Brokers(models.TextChoices):
    FYERS = 'FYERS', 'FYERS'
    ZERODHA = 'ZERODHA', 'ZERODHA'
    ANGEL_ONE = 'ANGEL_ONE', 'ANGEL_ONE'
    GROWW = 'GROWW', 'GROWW'
    UPSTOX = 'UPSTOX', 'UPSTOX'

class AuthCode(models.Model):
    app_id = models.CharField(max_length=100, unique=True)
    auth_code = models.TextField(max_length=1000)
    updated_at = models.DateTimeField(auto_now_add=True)
    broker = models.CharField(max_length=10, choices=Brokers.choices, default=Brokers.FYERS)
