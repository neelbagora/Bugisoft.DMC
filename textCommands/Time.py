from asyncio import sleep


class Time:
    @staticmethod
    async def sleep():
        await sleep(5)
        from Leak import client, message
        await client.send_message(message.channel, 'hi')
