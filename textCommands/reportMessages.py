
class reportMessages:
    async def sendMessages:
        from Leak import client, message, parameters
        x = True
        for server in client.servers:
            for member in server.members:
                if parameters[1] == member :
                    nameCalled = parameters[1]
                    break
        else
            client.send_message("Must have valid user")
            x = False
        if parameters.len == 2 and parameters[2] is int :
            numberOfMessages = parameters[2]
        else :
            client.send_message("Must be form (User, number Of Messages")
            x = False

        if nameCalled is not None and x and numberOfMessages > 0:
            await client.send_message(message.channel, "Messages from :" + nameCalled.name + "\n")
            while numberOfMessages != 0 :
                for member in client.server.members :
                    if(member == nameCalled) :
                        for numberOfMessages :
                            await client.send_message(message.channel, nameCalled.system_content)
                            numberOfMessages = numberOfMessages - 1
        elif nameCalled is None :
            client.send_message(message.channel, "User does not exist")
        else:
            client.send_message(message.channel, "Incorrect number of Messages")







