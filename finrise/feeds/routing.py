from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path(r'live-feed/subscribe/',
         consumers.LiveFeedConsumer.as_asgi()),
]