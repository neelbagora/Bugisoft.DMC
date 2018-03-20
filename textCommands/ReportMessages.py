from Leak import client, message, parameters
from collections import deque


class reportMessages:
    @staticmethod
    async def sendMessages():
        for member in message.server.members:
            if parameters[1] == member.id:
                print(parameters[1] + " " + member.id)
                break
            else:
                await client.send_message(message.channel, "Must have valid user")
                return
        if parameters.len is not 2 or parameters[2] is not int:
            await client.send_message(message.channel, "Must be form (User, number Of Messages")

        messages = deque()
        if parameters[2] > 0:
            await client.send_message(message.channel, "!!!")
            await client.send_message(message.channel, "Messages from :" + parameters[1].name)
            for m in message:
                if m.author is parameters[1]:
                    messages.appendleft(m)
                    if len(messages > parameters[2]):
                        messages.pop()
        for i in messages:
            await client.send_message(message.channel, i)
