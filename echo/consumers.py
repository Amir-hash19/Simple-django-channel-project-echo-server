from channels.generic.websocket import AsyncWebsocketConsumer
import json

class EnchoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data=None ,bytes_data=None):
        if text_data:
            await self.send(text_data=text_data)
        elif bytes_data:
            await self.send(bytes_data=bytes_data)    
