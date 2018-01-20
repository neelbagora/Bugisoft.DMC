from asyncio import sleep, async
from collections import deque


class MusicQue:

    musicQue = deque()

    @staticmethod
    async def add(songURL):
        MusicQue.musicQue.append(songURL)

    @staticmethod
    async def pop():
        return await MusicQue.musicQue.popleft()
