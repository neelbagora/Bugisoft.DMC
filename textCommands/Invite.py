class Invite:
    @staticmethod
    async def create_invite():
        from Leak import client
        from Leak import message
        from Leak import parameters
        if (parameters[1] != None):
            link = await client.create_invite(message.channel, max_age=60, max_uses=1, temporary=False, unique=True)
        else:
            link = await client.create_invite(message.channel, max_age=parameters[1]*60, max_uses=1, temporary=False, unique=True)
        await client.send_message(message.channel, link)
        await client.delete_message(message)
