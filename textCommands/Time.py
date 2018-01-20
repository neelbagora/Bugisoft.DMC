from asyncio import sleep


class Time:

    def __init__(self, client):
        self.defaultTimerMin = 60
        self.defaultTimerSec = 0
        self.client = client

    async def sleep(self, message):
        await sleep(5)

        await self.client.send_message(message.channel, 'hi')
