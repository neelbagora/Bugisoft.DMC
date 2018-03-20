async def ping():
    from Leak import client, message
    pong_message = await client.send_message(message.channel, "Pong!")
    from asyncio import sleep
    await sleep(5)
    await client.delete_message(pong_message)
