class Invite:
    @staticmethod
    async def create_invite():
        from Leak import client
        from Leak import message
        from Leak import parameters
        if len(parameters) == 1:
            time = 60
            link = await client.create_invite(message.channel, max_age=60, max_uses=1, temporary=False, unique=True)
        else:
            time = int(parameters[1]) * 60
            link = await client.create_invite(message.channel, max_age=time, max_uses=1, temporary=False, unique=True)
        invitemessage = await client.send_message(message.channel, link)
        await client.delete_message(message)
        from asyncio import sleep
        await sleep(time)
        await client.delete_message(invitemessage)
