from collections import deque


class MusicQue:
    musicQue = deque()

    @staticmethod
    async def add():
        from Leak import parameters
        MusicQue.musicQue.append(parameters[1])

    @staticmethod
    async def pop():
        return await MusicQue.musicQue.popleft()

    @staticmethod
    async def removeSingle():
        from Leak import parameters
        await MusicQue.musicQue.index(parameters[1])

    @staticmethod
    async def removeMultiple():
        from Leak import parameters
        await MusicQue.musicQue.index(None, parameters[1], parameters[2])

    @staticmethod
    async def list():
        None