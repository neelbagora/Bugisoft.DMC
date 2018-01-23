class Ping:

    @staticmethod async def pingbot(client, message):
        await client.send_message(message.channel, "Pong!")
