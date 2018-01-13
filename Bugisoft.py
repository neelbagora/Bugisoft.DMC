import discord
import asyncio

#
import logging
logging.basicConfig(level=logging.INFO)
#

#Imports command libraries.
#exec(open('config.txt').read())
#if (text):
#    from textCommands import ping

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    if message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    if message.content.startswith('!ping'):
        await client.send_message(message.channel, 'pong')
    if message.content.startswith('!stop'):
        client.close

exec(open('credentials.txt').read())
client.run(bot_token)