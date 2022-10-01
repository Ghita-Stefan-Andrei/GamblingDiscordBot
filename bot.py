import discord
import commands as cm
import pacaneaFruits as pf
import random

TOKEN = ''
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} is now running.')

@client.event
async def on_message(message):
    #if message.author == client.user:
        #return
    user = str(message.author)
    mess = str(message.content)
    channel = message.channel
    try:
        await cm.command[mess.split()[0]](message, user, channel)
    except Exception as e:
        pass#print(e)
    
    if message.content == "Double or nothing?":
        await message.add_reaction("\U0001F44D") #yes
        await message.add_reaction("\U0001F44E") #no
    
    if message.content == ":grey_question::grey_question::grey_question:":
        await message.add_reaction("\U0001F534")  #red
        await message.add_reaction("\U000026AB")  #black
        await message.add_reaction("\U0001F501")

    if message.content == "Better luck next time":
        await message.add_reaction("\U0001F501")

@client.event
async def on_reaction_add(reaction, user):
    if str(reaction.message.channel.id) == pf.pacChannel and reaction.count > 1: #reaction.message.author != client.user:
        if reaction.emoji == "\U0001F44E":
            pf.credit += pf.winnings
            pf.winnings = 0
            await reaction.message.channel.send(f':dollar: New Balance :dollar: : {pf.credit}')
            await cm.command[f'{pf.commTag}roll'](reaction.message, reaction.message.author, reaction.message.channel)
        if reaction.emoji == "\U0001F44D":
            pf.dublaj = 1
            await reaction.message.channel.send(":grey_question::grey_question::grey_question:")
        
        if reaction.emoji == "\U0001F534" or reaction.emoji == "\U000026AB":
            nr = random.randint(0,1)
            colDict = dict()
            colDict[0] = "\U0001F534"
            colDict[1] = "\U000026AB"
            if reaction.emoji == colDict[nr]:
                pf.winnings *= 2
                await reaction.message.channel.send(f'You guessed right it was {colDict[nr]}')
                await reaction.message.channel.send(":grey_question::grey_question::grey_question:")
            else:
                pf.winnings = 0
                await reaction.message.channel.send(f'You guessed wrong it was {colDict[nr]}')
                await reaction.message.channel.send("You lost")
                await cm.command[f'{pf.commTag}roll'](reaction.message, reaction.message.author, reaction.message.channel)
        
        if reaction.emoji == "\U0001F501":
            await cm.command[f'{pf.commTag}roll'](reaction.message, reaction.message.author, reaction.message.channel)
            
client.run(TOKEN)
