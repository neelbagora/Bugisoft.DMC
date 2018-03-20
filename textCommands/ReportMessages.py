from Leak import client, message, parameters
from collections import deque

from passives.TextFormatter import TextFormatter


class reportMessages:
    @staticmethod
    async def sendMessages():
        id = parameters[1]
        id = TextFormatter.format_mention_to_id(id)
        found = False
        for member in message.server.members:
            print(id + " " + member.id)
            if id == member.id:
                found = True
                break

        if not found:
            await client.send_message(message.channel, "Must have valid user")
            return

        if len(parameters) is not 3 or parameters[2] is not int:
            await client.send_message(message.channel, "Must be form (User, number Of Messages")

        messages = deque()
        if parameters[2] > 0:
            await client.send_message(message.channel, "!!!")
            await client.send_message(message.channel, "Messages from :" + parameters[1].name)
            for m in message:
                if m.author is id:
                    messages.appendleft(m)
                    if len(messages) > parameters[2]:
                        messages.pop()
        for i in messages:
            await client.send_message(message.channel, i)
