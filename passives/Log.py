from datetime import datetime


class Log:

    fileName = None

    @staticmethod
    async def addline():
        file = open(Log.fileName, 'a')

        from Leak import message
        file.write(str(message.timestamp) + ": " + str(message.author) + ": " + str(
            message.content) + "\n")
        file.close()

    @staticmethod
    async def init():
        Log.fileName = "/home/bugisoft/logs/log-%s" % datetime.now().isoformat()
