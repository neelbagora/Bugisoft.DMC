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
