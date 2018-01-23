import Bugisoft
from voiceCommands.MusicPlayer import MusicPlayer


class VoiceConnector:

    voice = None

    @staticmethod
    async def join(channel):
        VoiceConnector.voice = await Bugisoft.client.join_voice_channel(channel)
        await MusicPlayer.init(VoiceConnector.voice)

    @staticmethod
    async def leave():
        await VoiceConnector.voice.disconnect()
