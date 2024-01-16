from django.urls import path
from .views import WebhookDataView

urlpatterns = [
    path('webhook/', WebhookDataView.as_view(), name='webhook'),
]
