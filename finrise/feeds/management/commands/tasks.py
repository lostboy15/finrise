from django.core.management.base import BaseCommand

import websockets
import asyncio
from feeds.constants import Binance_WS_API
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


async def create_ws(url):

    async with websockets.connect(url) as websocket:
        while True:
            message = await websocket.recv()
            if message:
                channel_layer = get_channel_layer()
                await channel_layer.group_send(   # sending live feed to all the open web socket connection
                    'binance_live_feed',
                    {'type': "feed_message", 'message': message}
                )


class Command(BaseCommand):

    def handle(self, *args, **options):
        asyncio.run(create_ws(Binance_WS_API))