from asyncio import sleep

from voiceCommands.MusicQue import MusicQue


class MusicPlayer:
    voice = None
    player = None

    @staticmethod
    async def init(voice):
        MusicPlayer.voice = voice
        MusicPlayer.player = await MusicPlayer.voice.create_ytdl_player('https://www.youtube.com/watch?v=MqRhQe6oaJA')
        await MusicPlayer.start()
        await MusicPlayer.play()

    @staticmethod
    async def start():
        MusicPlayer.player.start()

    @staticmethod
    async def pause():
        MusicPlayer.player.pause()

    @staticmethod
    async def unpause():
        MusicPlayer.player.resume()

    @staticmethod
    async def play():
        while True:
            if MusicPlayer.player.is_done() and len(MusicQue.musicQue) > 0:
                nextSong = MusicQue.musicQue.popleft()
                if nextSong != '':
                    MusicPlayer.player = await MusicPlayer.voice.create_ytdl_player(nextSong)
                    MusicPlayer.player.start()
            await sleep(1)

    @staticmethod
    async def clear():
        MusicQue.musicQue.clear()
