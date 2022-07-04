import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = 'jm!')
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Sonic Riders | jm!help'))
    print("Jet mini is ready")

@client.command()
async def help(ctx):
    await ctx.send("LIST OF JET THE HAWK MINI BOt COMMANDS\nPrefix: jm!\n\njm!help - This message\njm!info - Information about the bot\njm!jetsong - Links you to the Them Song of Jet the Hawk\njm!jetpic - Random Jet the Hawk Picture")

@client.command()
async def info(ctx):
    await ctx.send("Jet the Hawk Mini\nMade with: discord.py / Python\nMade by: Jet The Hawk Main#8960")

@client.command()
async def jetsong(ctx):
    await ctx.send("My theme song: https://www.youtube.com/watch?v=twzpqI5fMyU")

@client.command()
async def ownermedia(ctx):
    await ctx.send("Here is the bot creator's social media\nYoutube: https://www.youtube.com/channel/UC0t2jbH82Kr_8mh-IDwUgjQ\nTwitter: https://twitter.com/JettheHawk18")

@client.command()
async def jetpic(ctx):
    responses = ["jet1.jpg",
                 "jet2.jpg",
                 "jet3.jpg",
                 "jet4.jpg",
                 "jet5.jpg",
                 "jet6.jpg",
                 "jet7.png",
                 "jet8.jpg",
                 "jet9.jpg",
                 "jet10.jpg",
                 "jet11.jpg",]
    await ctx.send(file=discord.File(f'./images/{random.choice(responses)}'))




client.run("BOT TOKEN HERE")
