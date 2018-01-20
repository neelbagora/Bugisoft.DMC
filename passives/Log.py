from datetime import datetime


class Log:

    def __init__(self):
        self.filename = ("/home/bugisoft/logs/log-%s" % datetime.now().isoformat())

    async def addline(self, message):
        file = open(self.filename, 'a')
        file.write(str(message.timestamp) + ": " + str(message.author) + ": " + str(message.content) + "\n")
        file.close()
