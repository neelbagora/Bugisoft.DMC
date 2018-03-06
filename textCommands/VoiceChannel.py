class VoiceChannel:
    @staticmethod
    async def create_channel():
        from Leak import client
        from Leak import message
        from Leak import parameters
        if len(parameters) == 1:
            import discord
            channel = await client.create_channel(message.server, 'Voice', type=discord.ChannelType.voice)
        else:
            import discord
            channel = await client.create_channel(message.server, parameters[1], type=discord.ChannelType.voice)
        client.edit_channel(channel, bitrate=96000)
        await client.delete_message(message)
