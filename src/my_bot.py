import random
from discord.ext.commands import Bot
from values import *

prefix = ("!", "$")
client = Bot(command_prefix=prefix)
lineList = [line.rstrip('\n') for line in open('./resources/insults.txt')]
# Create all bot commands after here


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.listen()
async def on_message(ctx):
    print(f"Received message {ctx.content}")
    if ctx.author.id == (Bubbles or  Mechro):
        await ctx.channel.send("You a bitch!")
    elif ctx.author.id == (Mason or Maurice):
        await ctx.channel.send(random.choice(lineList))
    messageStart = ctx.content.lower()
    question = "Is this the krusty krab?"
    if messageStart.startswith('$hello') or messageStart.startswith('!hello'):
        await ctx.channel.send('Hello!')
    if messageStart.startswith('$bot') or messageStart.startswith('!bot'):
        await ctx.channel.send('You rang?')
    if question in messageStart:
        await ctx.channel.send('No, this is Patrick...')

@client.command(name='praise')
async def test_command(ctx):
    if ctx.author.id == Me:
        await ctx.send("Hail the Almighty!")

@client.command(name='test')
async def test_command(ctx):
    await ctx.send("ahhhhhh")

@client.command(name='roast')
async def roast_command(ctx):
    if(ctx.author == "1up Mason#5427" or ctx.author == "Maurice's Puffs#6232"):
        return
    else:
        await ctx.send(random.choice(lineList))

@client.command(name='shutdown')
async def shutdown(ctx):
    if ctx.author.id == Me:
        await ctx.bot.logout()

client.run(token)