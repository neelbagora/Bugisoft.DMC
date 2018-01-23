class Ping:

    @staticmethod
    async def pingbot():
        from Leak import client, message
        await client.send_message(message.channel, "Pong!")
