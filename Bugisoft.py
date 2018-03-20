from collections import deque

import discord

import Leak

client = discord.Client()

# Config and Credential Vars
loggerEnabled = None
bot_token = None

# Leaked Vars
Leak.client = client
Leak.messageArr = deque()


@client.async_event
async def on_ready():
    from passives.Log import Log
    await Log.init()


@client.async_event
async def on_message(message):
    Leak.message = message
    Leak.messageArr.appendleft(message)

    # Logging
    if loggerEnabled:
        from passives.Log import Log
        await Log.addline()

    # Confirms User Is Not Bot and Filters Out Non Bot Messages
    if message.author == client.user or not message.content.startswith('!'):
        return

    # Formats Text
    from passives.TextFormatter import TextFormatter
    parameters = TextFormatter.formatMessageToParameters()
    Leak.parameters = parameters
    print(parameters)

    await client.delete_message(message)

    # TEXT COMMANDS
    # Help
    if parameters[0] == 'help':
        from textCommands.Help import Help
        await Help.display_help()

    elif parameters[0] == 'ping':
        from textCommands.Ping import ping
        await ping()

    elif parameters[0] == 'join':
        from voiceCommands.VoiceConnecter import VoiceConnector
        await VoiceConnector.join()

    elif parameters[0] == 'leave':
        from voiceCommands.VoiceConnecter import VoiceConnector
        await VoiceConnector.leave()

    elif parameters[0] == 'pause':
        from voiceCommands.MusicPlayer import MusicPlayer
        await MusicPlayer.pause()

    elif parameters[0] == 'unpause':
        from voiceCommands.MusicPlayer import MusicPlayer
        await MusicPlayer.unpause()

    elif parameters[0] == 'clear':
        from voiceCommands.MusicPlayer import MusicPlayer
        await MusicPlayer.clear()

    elif parameters[0] == 'que' or parameters[0] == 'play':
        from voiceCommands.MusicQue import MusicQue
        await MusicQue.add()

    elif parameters[0] == 'sleep':
        from textCommands.Time import Time
        await Time.sleep()

    elif parameters[0] == 'invite':
        from textCommands.Invite import Invite
        await Invite.create_invite()

    elif parameters[0] == 'open':
        from textCommands.VoiceChannel import VoiceChannel
        await VoiceChannel.create_channel()

    elif parameters[0] == 'close':
        from textCommands.VoiceChannel import VoiceChannel
        await VoiceChannel.remove_empty_channels()

    elif parameters[0] == 'log':
        from textCommands.ReportMessages import reportMessages
        await reportMessages.sendMessages()

    if message.author.id != 119978889891151876:
        return

    if parameters[0] == 'update':
        from adminCommands.Update import Update
        await Update.update()


@client.async_event
async def on_voice_state_update(before, after):
    if before.voice.voice_channel is not None and after is None:
        from textCommands.VoiceChannel import VoiceChannel
        await VoiceChannel.remove_empty_channels()


exec(open('config.txt').read())
exec(open('credentials.txt').read())

client.run(bot_token)
