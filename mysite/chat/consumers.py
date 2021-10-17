import json
from channels.generic.websocket import WebsocketConsumer

message=0
class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        global message

        text_data_json = json.loads(text_data)
        val=message
        message = int(text_data_json['message'])+message
        self.send(text_data=json.dumps({
            'message': message,
            'val':val
            
        }))
