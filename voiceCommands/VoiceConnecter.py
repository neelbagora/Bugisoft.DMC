from voiceCommands.MusicPlayer import MusicPlayer


class VoiceConnector:

    voice = None

    def __init__(self):
        self.channelID = 0

    @staticmethod
    async def join(client, channel):
        VoiceConnector.voice = await client.join_voice_channel(channel)
        await MusicPlayer.init(VoiceConnector.voice)

    @staticmethod
    async def leave():
        await VoiceConnector.voice.disconnect()
