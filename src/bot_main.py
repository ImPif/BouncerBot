import discord

from values import *

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    messageStart = message.content.lower()
    question = "Is this the krusty krab?"
    if messageStart.startswith('$hello'):
        await message.channel.send('Hello!')
    if messageStart.startswith('$bot'):
        await message.channel.send('You rang?')
    if question in messageStart:
        await message.channel.send('No, this is Patrick...')

client.run(token)