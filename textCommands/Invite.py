class Invite:
    @staticmethod
    async def create_invite():
        from Leak import client
        from Leak import message
        inviteLink = await client.create_invite(message.channel, max_age=60, max_uses=1, temporary=False, unique=True)
        await client.send_message(message.channel, inviteLink)
        await client.delete_message(message)
