from asyncio import sleep

import discord

from passives.Log import Log
from textCommands.Ping import Ping

client = discord.Client()

# Command Instances
logger = Log()
pinger = Ping(client)


@client.event
async def on_message(message):
    # Logging
    if loggerEnabled:
        await logger.addline(message)

    # Confirms User Is Not Bot
    if message.author == client.user:
        return

    # Confirms Prefix
    if not message.content.startswith('!'):
        return

    # TEXT COMMANDS
    # Help
    if message.content.startswith('!help'):
        client.send_message("```Help Commands:```")

    # Timer Command
    if message.content.startswith('!sleep'):
        message.content
        await sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    if message.content.startswith('!ping'):
        await pinger.pingbot(message)

    # VOICE COMMANDS

    if message.content.startswith('!join'):
        client.join_voice_channel()


#    if message.content.startswith('!delete'):

exec(open('config.txt').read())
exec(open('credentials.txt').read())

client.run(bot_token)
