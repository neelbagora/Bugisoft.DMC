from datetime import datetime


class Log:

    def __init__(self):
        self.filename = ("log-%s" % datetime.now().isoformat())

    async def addline(self, message):
        file = open(self.filename, 'a')
        file.write(str(message))
        file.close()
