import discord

from passives.Log import Log
from passives.TextFormatter import TextFormatter
from textCommands.Ping import Ping
from textCommands.Time import Time
from voiceCommands.MusicPlayer import MusicPlayer
from voiceCommands.MusicQue import MusicQue
from voiceCommands.VoiceConnecter import VoiceConnector

client = discord.Client()

# Command Instances
logger = Log()
pinger = Ping(client)
timer = Time(client)
textFormatter = TextFormatter()
voiceConnector = VoiceConnector()


@client.event
async def on_message(message):
    # Logging
    global musicPlayer
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
    print(parameters)

    # TEXT COMMANDS
    # Help
    if parameters[0] == 'help':
        client.send_message("```Help Commands:```")

    # Timer Commands
    if parameters[0] == 'sleep':
        await timer.sleep(message, parameters)

    # Ping
    if parameters[0] == 'ping':
        await pinger.pingbot(message)

    if parameters[0] == 'join':
        await voiceConnector.join(client, message.author.voice_channel)

    if parameters[0] == 'leave':
        await voiceConnector.leave()

    if parameters[0] == 'pause':
        await MusicPlayer.pause()

    if parameters[0] == 'unpause':
        await MusicPlayer.unpause()

    if parameters[0] == 'clear':
        await MusicPlayer.clear()

    if parameters[0] == 'que':
        await MusicQue.add(parameters[1])


exec(open('config.txt').read())
exec(open('credentials.txt').read())

client.run(bot_token)
