from twitch import TwitchClient
import discord
import asyncio

CLIENT_ID = 'n9fj9vtnet647vjx7upm31ftwvu335'
FRVMED_ID = '192336272'
TOKEN = 'NDMwNTQ1MDk5NTcxNTkzMjM2.DaR0eA.b_05RLFLSw24iHsL64ei5pIIToA'

#192336272 framed
#55039613 Arms dude
#26490481 Fortnite dude

# DISCORD
discordClient = discord.Client()

# TWITCH
client = TwitchClient(client_id=CLIENT_ID)
channel = client.channels.get_by_id(FRVMED_ID)

# checking stream
def stream():
    streamStatus = client.streams.get_stream_by_user(FRVMED_ID)
    if streamStatus is not None:
        notif = channel.display_name
        return notif
    else:
        return

@discordClient.event
async def on_ready():
    print('Logged in as')
    print(discordClient.user.name)
    print(discordClient.user.id)
    print('--------')

@discordClient.event
async def on_message(message):
    if message.author == discordClient.user:
        return
    if message.content.startswith('!hello'):
        msg = 'Wasup hot boi {0.author.mention}'.format(message)
        await discordClient.send_message(message.channel, msg)
    if message.content.startswith('!bye'):
        msg = 'See ya! {0.author.mention}'.format(message)
        await discordClient.send_message(message.channel, msg)

async def stream_check():
    await discordClient.wait_until_ready()
    streaming = False
    while not discordClient.is_closed:
        print ('checking stream...')
        stream()
        status = stream()
        print (status)
        if streaming == False:
            if status is not None:
                msg = channel.display_name + ' is streaming! yay!'
                streaming = True
                print ('client started stream')
                await discordClient.send_message(discordClient.get_channel('430546424296505345'), msg)
            else:
                print ('not streaming')
        if streaming == True:
            if status is None:
                msg = channel.display_name + ' stopped streaming, see ya next time.'
                streaming = False
                print ('client stopped stream.')
                await discordClient.send_message(discordClient.get_channel('430546424296505345'), msg)
        await asyncio.sleep(5)

discordClient.loop.create_task(stream_check())
discordClient.run(TOKEN)
