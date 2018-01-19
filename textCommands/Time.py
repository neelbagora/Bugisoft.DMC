class Time:

    def __init__(self, client):
        self.defaultTimerMin = 60
        self.defaultTimerSec = 0

    async def pingbot(self, message):
        await self.client.send_message(message.channel, self.returnstatement)