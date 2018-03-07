class VoiceChannel:

    channel_list = []

    @staticmethod
    async def create_channel():
        from Leak import client
        from Leak import message
        from Leak import parameters
        channel_max_users = 0
        if len(parameters) == 1:
            channel_name = "Voice"
        elif len(parameters) == 2:
            channel_name = parameters[1]
        else:
            channel_name = parameters[1]
            channel_max_users = parameters[2]
        import discord
        channel = await client.create_channel(message.server, channel_name, type=discord.ChannelType.voice)
        VoiceChannel.channel_list.append(channel)
        await client.edit_channel(channel, bitrate=96000, user_limit=channel_max_users)
        await client.move_member(message.author, channel)

    @staticmethod
    async def remove_empty_channels():
        for channel in VoiceChannel.channel_list:
            if len(channel.voice_members) is 0:
                from Leak import client
                from Leak import message
                VoiceChannel.channel_list.remove(channel)
                await client.delete_channel(channel)
                await VoiceChannel.remove_empty_channels()
