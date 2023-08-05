import discord
from discord.ext import commands
import random
import asyncio

client = commands.Bot(command_prefix = 'j!')
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Sonic Riders | j!help'))
    print("Jet the Hawk is ready")



@client.command()
async def help(ctx):
    embed = discord.Embed(title="Jet the Hawk Bot Information", description="LIST OF JET THE HAWK BOT COMMANDS\nPrefix: j!", color=(65359))
    embed.add_field(name="GENERAL", value='j!help - This message\nj!info - Information about the bot', inline=False)
    embed.add_field(name="FUN COMMANDS", value='j!askjet - Ask Jet the Hawk stuff\nj!jetpic - I send a picture of Jet the Hawk\nj!jetwallpaper - I give you a Jet the Hawk wallpaper\nj!playjetstheme - I play Jet The Hawks theme song in VC\nj!celebrate - Plays the Sonic CD Zone Clear Jingle', inline=False)
    embed.add_field(name="UTILITY", value='j!jetstheme - Links you to the Theme Song of Jet the Hawk\nj!say - Make the bot say your message\nj!esay - Make the bot say stuff in a embed', inline=False)
    embed.add_field(name="INVITE ME", value='[Invite me](https://discord.com/oauth2/authorize?client_id=999908333215551580&permissions=0&scope=bot)', inline=False)
    await ctx.send(embed=embed)

@client.command()
async def info(ctx):
    embed = discord.Embed(title="Jet the Hawk Bot Information", description="Information about this bot. My prefix is **j!**", color=(65359))
    embed.add_field(name="STATUS", value=f'Made with: discord.py\nMade by: Jet the Hawk#8960\nLatency: {round(client.latency * 1000)}ms\nServers I am in: {len(client.guilds)}', inline=False)
    embed.add_field(name="LINKS", value='INVITE THE BOT: https://discord.com/oauth2/authorize?client_id=999908333215551580&permissions=0&scope=bot\nSupport Server: https://discord.gg/c7MnZDn4RS\nSource Code: https://github.com/JetTheHawk18/JetTheHawkBot', inline=False)
    embed.add_field(name="OWNERS SOCIAL MEDIA", value='Here is the bot creators social media\nYoutube: https://www.youtube.com/channel/UC0t2jbH82Kr_8mh-IDwUgjQ\nTwitter: https://twitter.com/JettheHawk18', inline=False)
    await ctx.send(embed=embed)

@client.command()
async def jetstheme(ctx):
    await ctx.send("My theme song: https://www.youtube.com/watch?v=twzpqI5fMyU")

@client.command()
async def say(ctx, *, question: commands.clean_content):
    await ctx.send(f'{question}')
    await ctx.message.delete()

@say.error
async def say_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("What do you want me to say?")
    else:
        raise error

@client.command()
async def esay(ctx, *, question):
    embed = discord.Embed(description=f'{question}', color=(65359))
    await ctx.send(embed=embed)
    await ctx.message.delete()

@esay.error
async def esay_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("What do you want me to say?")
    else:
        raise error

@client.command(aliases=["askjet"])
async def chat(ctx, *, question):
    responses = ["Enjoy those dreams while you still can!",
                 "Maybe you better walk him through it, Wave.",
                 "I'm No. 1",
                 "Next time, you won't be so lucky",
                 "You sure you wanna risk a rematch? I promise you right now you'll regret it!",
                 "Ugh, the both of you are useless. Looks like I'm going to have to get serious if we want to win this!",
                 "Yaaawn, can the boring speech! What can this thing do for me",
                 "Ugh! I'll get you next time!",
                 "Hmph! I lost! So don't play games with me! I don't want your pity, nor do I need it!",
                 "The dirt suits you so well!"]
    await ctx.send(f'Question: {question}\nJet the Hawks Answer: {random.choice(responses)}', allowed_mentions=discord.AllowedMentions(roles=False, users=True, everyone=False))

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
                 "jet11.jpg",
                 "jet12.png",
                 "jet13.jpg",
                 "jet14.png",
                 "jet15.png",
                 "jet16.jpg",
                 "jet17.jpg",]
    await ctx.send(file=discord.File(f'./images/{random.choice(responses)}'))

@client.command()
async def jetwallpaper(ctx):
    responses = ["wallpaper1.jpg",
                 "wallpaper2.png",
                 "wallpaper3.jpg",
                 "wallpaper4.png",
                 "wallpaper5.png",
                 "wallpaper6.png",
                 "wallpaper7.png",
                 "wallpaper8.jpg",
                 "wallpaper9.jpg",]
    await ctx.send(file=discord.File(f'./images/{random.choice(responses)}'))

@client.command()
async def playjetstheme(ctx):
    voice = await ctx.author.voice.channel.connect()
    voice.play(discord.FFmpegPCMAudio('./images/jetstheme.mp3'))
    await ctx.send("I am now playing my own theme song")
    await asyncio.sleep(225)
    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command()
async def celebrate(ctx):
    voice = await ctx.author.voice.channel.connect()
    voice.play(discord.FFmpegPCMAudio('./images/soniccdpass.mp3'))
    await asyncio.sleep(10)
    server = ctx.message.guild.voice_client
    await server.disconnect()

@client.command(aliases=["leave"])
async def stop(ctx):
    server = ctx.message.guild.voice_client
    await server.disconnect()
    await ctx.send("Ok. I stopped the music")





client.run("BOTTOKENHERE")
