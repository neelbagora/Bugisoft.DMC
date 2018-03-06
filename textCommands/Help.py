class Help:
    @staticmethod
    async def display_help():
        from Leak import client
        from Leak import message
        help_message = await client.send_message(message.channel, "Help:\n"
                                                                  "!invite (optional-time)\n")
        await client.delete_message(message)
        from asyncio import sleep
        await sleep(30)
        await client.delete_message(help_message)
