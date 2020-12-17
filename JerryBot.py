import random
import discord
from discord.ext import commands
bad_word = []
good_word = []
leaderboard = {}
txt1 = open(file='badwords.txt')
for words in txt1.read().split():
    bad_word.append(words)
client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    

@client.event
async def on_memember_join(member):
    print(f'{member} has joined, give them a warm welcome!')
    channel = discord.utils.get(member.guild.text_channels, name="general")
    await channel.send(f'{member} has joined, give them a warm welcome!')    

@client.event
async def on_memember_removed(member):
    print(f'{member} was wack and left.')
    channel = discord.utils.get(member.guild.text_channels, name="general")
    await channel.send(f'{member} was wack and left.')    

@client.event
async def on_message(message):
    count = 0
    check = message.author
    said = []
    split = message.content.split()
    if message.content.startswith('.'):
        pass
    else:
        if check != '': #Enter your bot's username here so it won't have an infinite loop when your bot repeats the word 
            for i in range(len(bad_word)):
                for x in split:
                    if bad_word[i] == x:
                        said.append(bad_word[i])
                        count = count + 1
            if count > 0:
                said1 =''
                for i in said:
                    said1 += i + ', '
                await message.channel.send(f"Oooo {message.author} just typed {said1}! That's +{count} for you!")
                if message.author in leaderboard:
                    leaderboard[message.author] = leaderboard[message.author] + count
                    await message.channel.send(f"{message.author} you have {leaderboard[message.author]} rude points now!")
                else:
                    leaderboard[message.author] = count
    await client.process_commands(message)

@client.command(aliases=['leaderboard','lb'])
async def leader(ctx):
    await ctx.message.channel.send("These are the rudest nerds on the server!")
    sorted_dic = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    for key, value in sorted_dic:
        await ctx.message.channel.send("{} : {}".format(key,value))


client.run("Enter your bot code here")
