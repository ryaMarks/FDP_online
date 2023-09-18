import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync



class ChatConsumer(WebsocketConsumer):
    # ao cliente se conectar 
    def connect(self):
        self.public_group_name = 'test'
        self.private_group_name = 'private_room'
        async_to_sync(self.channel_layer.group_add)(
            self.public_group_name,
            self.channel_name 
        )
        self.accept()

        # envia mensagem de conexão ao cliente
        self.send(text_data=json.dumps({
            'type':'connection_established',
            'message': 'Tu se conectou no grupo '
        }))

    def disconnect(self, close_code):
        # Remover o cliente do grupo quando ele desconectar
        self.channel_layer.group_discard(
            self.public_group_name,
            self.channel_name
        )
    
    # recebe mensagens do cliente
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        if message == "conectar":
            # Remover o cliente do grupo publico
            self.channel_layer.group_discard(
                self.public_group_name,
                self.channel_name
            )

            # adiciona o cliente ao grupo privado
            '''
            async_to_sync(self.channel_layer.group_add)(
                self.private_group_name,
                self.channel_name 
            )'''    

        else:
            async_to_sync(self.channel_layer.group_send)(
                self.private_group_name,
                {
                    'type': 'chat_message',
                    'message': message
                }
            )

    # envia mensagens ao cliente
    def chat_message(self, event):
        message = event['message']
        self.send(text_data = json.dumps({
            'type': 'chat',
            'message': message
        }))
        
