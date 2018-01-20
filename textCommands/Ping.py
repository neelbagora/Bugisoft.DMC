class Ping:

    def __init__(self, client):
        self.returnstatement = "Pong!"
        self.client = client

    async def pingbot(self, message):
        await self.client.send_message(message.channel, self.returnstatement)
