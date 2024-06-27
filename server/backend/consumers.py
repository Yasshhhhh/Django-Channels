import json
from channels.generic.websocket import WebsocketConsumer

class MyConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            'message': 'Message From Socket On Connect!'
        }))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data=None):
        self.send(text_data=json.dumps({
            'message': 'Hello, world!'
        }))
