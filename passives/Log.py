from datetime import datetime


class Log:

    @staticmethod
    async def addline(message):
        file = open("/home/bugisoft/logs/log-%s" % datetime.now().isoformat(), 'a')
        file.write(str(message.timestamp) + ": " + str(message.author) + ": " + str(message.content) + "\n")
        file.close()
