import discord

import Leak
from passives.Log import Log
from passives.TextFormatter import TextFormatter
from textCommands.Help import Help
from textCommands.Ping import Ping
from textCommands.Time import Time
from voiceCommands.MusicPlayer import MusicPlayer
from voiceCommands.MusicQue import MusicQue
from voiceCommands.VoiceConnecter import VoiceConnector
from textCommands.Invite import Invite
from textCommands.VoiceChannel import VoiceChannel

client = discord.Client()

# Config and Credential Vars
loggerEnabled = None
bot_token = None

# Leaked Vars
Leak.client = client
Leak.message = None
Leak.parameters = None


@client.async_event
async def on_ready():
    await Log.init()


@client.async_event
async def on_message(message):
    Leak.message = message

    # Logging
    if loggerEnabled:
        await Log.addline()

    # Confirms User Is Not Bot and Filters Out Non Bot Messages
    if message.author == client.user or not message.content.startswith('!'):
        return

    # Formats Text
    parameters = TextFormatter.formatMessageToParameters()
    Leak.parameters = parameters
    print(parameters)

    await client.delete_message(message)

    # TEXT COMMANDS
    # Help
    if parameters[0] == 'help':
        await Help.display_help()

    elif parameters[0] == 'ping':
        await Ping.pingbot()

    elif parameters[0] == 'join':
        await VoiceConnector.join()

    elif parameters[0] == 'leave':
        await VoiceConnector.leave()

    elif parameters[0] == 'pause':
        await MusicPlayer.pause()

    elif parameters[0] == 'unpause':
        await MusicPlayer.unpause()

    elif parameters[0] == 'clear':
        await MusicPlayer.clear()

    elif parameters[0] == 'que' or parameters[0] == 'play':
        await MusicQue.add()

    elif parameters[0] == 'sleep':
        await Time.sleep()

    elif parameters[0] == 'invite':
        await Invite.create_invite()

    elif parameters[0] == 'open':
        await VoiceChannel.create_channel()

    elif parameters[0] == 'close':
        await VoiceChannel.remove_empty_channels()


@client.async_event
async def on_voice_state_update(before, after):
    if before.voice.voice_channel is not None:
        await VoiceChannel.remove_empty_channels()


exec(open('config.txt').read())
exec(open('credentials.txt').read())

client.run(bot_token)
