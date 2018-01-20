import discord

from passives.Log import Log
from passives.TextFormatter import TextFormatter
from textCommands.Ping import Ping
from textCommands.Time import Time

client = discord.Client()

# Command Instances
logger = Log()
pinger = Ping(client)
timer = Time(client)
textFormatter = TextFormatter()


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

    # Formats Text
    parameters = textFormatter.formatMessageToParameters(message)

    # TEXT COMMANDS
    # Help
    if parameters[0] == 'help':
        client.send_message("```Help Commands:```")

    # Timer Commands
    if message.content.startswith('!sleep'):
        await timer.sleep()

    # Ping
    if parameters[0] == 'ping':
        await pinger.pingbot(message)

    # VOICE COMMANDS

    if message.content.startswith('!join'):
        client.join_voice_channel()


#    if message.content.startswith('!delete'):

exec(open('config.txt').read())
exec(open('credentials.txt').read())

client.run(bot_token)
