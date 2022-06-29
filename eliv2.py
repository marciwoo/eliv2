from http import client
from turtle import title
from discord.ext import commands, tasks
from discord.embeds import Embed
import datetime
import discord
import random
from discord import colour
import os
import youtube_dl
from discord.errors import Forbidden
from discord import Member

client = discord.Client()
bot = commands.Bot(command_prefix=('liz ', 'Liz ','.', ',', '-','LIZ '), help_command=None, case_insensitive=True)
bot.remove_command('help')

hug_gifs = ["https://cdn.discordapp.com/attachments/795654835856211990/855443745061994499/SPOILER_ezgif.com-gif-maker5.gif","https://media.discordapp.net/attachments/836293474679783455/852058613396537354/ezgif.com-gif-maker_1.gif"]
hug_name = ['you have been hugged', 'hugs you']
kiss_gifs= ["https://media.discordapp.net/attachments/836293474679783455/852928265810477066/ezgif.com-gif-maker1.gif","https://cdn.discordapp.com/attachments/836293474679783455/847551494340739072/ezgif.com-gif-maker1.gif","https://cdn.discordapp.com/attachments/836293474679783455/847186103543136256/ezgif.com-gif-maker2.gif","https://media.discordapp.net/attachments/836293474679783455/893580351551729674/ezgif.com-gif-maker1.gif","https://media.discordapp.net/attachments/836293474679783455/893579657704779786/ezgif.com-gif-maker.gif"]
kiss_name= ['kissed']
heal_gifs= ["https://media.discordapp.net/attachments/836293474679783455/858284035923116042/ezgif.com-gif-maker5.gif","https://media.discordapp.net/attachments/795654835856211990/858064067062005770/ezgif.com-gif-maker1.gif","https://cdn.discordapp.com/attachments/797692748873596960/809408422474154004/ezgif.com-crop1.gif","https://cdn.discordapp.com/attachments/797692748873596960/809408422474154004/ezgif.com-crop1.gif","https://cdn.discordapp.com/attachments/752032389600903178/815619496186216448/ezgif.com-gif-maker.gif"] 
heal_names= ['healed']
pat_gifs= ["https://cdn.discordapp.com/attachments/752032389600903178/809370553135661106/ezgif.com-crop3.gif","https://media.discordapp.net/attachments/836293474679783455/913897236386181180/ezgif.com-gif-maker2.gif","https://media.discordapp.net/attachments/795654835856211990/858065141839822848/ezgif.com-gif-maker2.gif"]
pat_names= ['gave a pat']
punch_gifs= ["https://cdn.discordapp.com/attachments/836293474679783455/847561477657067580/ezgif.com-gif-maker2.gif"]
punch_names= ['punched', 'hit']
bully_gifs= ["https://cdn.discordapp.com/attachments/836293474679783455/847569890470658128/ezgif.com-gif-maker.gif","https://cdn.discordapp.com/attachments/752032389600903178/809372187651080232/ezgif.com-crop6.gif"]
bully_names= ['is bullying']
kill_gifs= ["https://media.discordapp.net/attachments/734099095228121130/815540579378790410/Gloxinia_pierces_Escanor_with_Basquias.gif"]
kill_names= ['killed', 'ended']
happy_gifs= ["https://cdn.discordapp.com/attachments/836293474679783455/847563209769877546/ezgif.com-gif-maker6.gif"]
happy_names= ['is happy', 'shows their happiness']
smile_gifs= ["https://cdn.discordapp.com/attachments/752032389600903178/809374487530962945/ezgif.com-crop1.gif","https://media.discordapp.net/attachments/734099095228121130/815539850589503498/tenor.gif"]
smile_names= ['is smiling']
sad_gifs= ["https://media.discordapp.net/attachments/836293474679783455/893932631496998972/ezgif.com-gif-maker22.gif","https://cdn.discordapp.com/attachments/836293474679783455/847563693956530236/ezgif.com-gif-maker7.gif","https://cdn.discordapp.com/attachments/752032389600903178/809373570387148800/ezgif.com-gif-maker.gif"]
sad_names= ['is sad', 'shows thier sadness']
cry_gifs= ["https://cdn.discordapp.com/attachments/836293474679783455/847562463708315658/ezgif.com-gif-maker4.gif","https://cdn.discordapp.com/attachments/836293474679783455/847565508324491274/ezgif.com-gif-maker.gif","https://cdn.discordapp.com/attachments/752032389600903178/809369833413017600/ezgif.com-crop.gif","https://cdn.discordapp.com/attachments/836293474679783455/847562787981885510/ezgif.com-gif-maker5.gif","https://media.discordapp.net/attachments/795654835856211990/861676839428685844/dfgdfghdfh_3.gif","https://media.discordapp.net/attachments/836293474679783455/860624626882314250/ezgif.com-gif-maker.gif","https://cdn.discordapp.com/attachments/752032389600903178/809371143596933130/ezgif.com-crop4.gif"]
cry_names= ['is crying']
sleepy_gifs= ["https://cdn.discordapp.com/attachments/752032389600903178/809377227464376320/ezgif.com-crop1.gif","https://c.tenor.com/JFPtQc7FkIgAAAAM/derier-seven-deadly-sins.gif"]
sleepy_names= ['is sleepy', 'is tired']
eat_gifs= ["https://cdn.discordapp.com/attachments/752032389600903178/809374078724734986/ezgif.com-crop.gif"]
eat_names= ['is eating']
blush_gifs= ["https://media.discordapp.net/attachments/836293474679783455/853736904619720704/ezgif.com-gif-maker8.gif"]
blush_names= ['is blushing', 'is flustered']
die_gifs= ["https://cdn.discordapp.com/attachments/836293474679783455/847560298549477396/ezgif.com-gif-maker1.gif"]
die_names= ['is dying', 'is dead', 'is sent to the otherworld']
shock_gifs= ["https://media.discordapp.net/attachments/836293474679783455/893932181683077210/ezgif.com-gif-maker3.gif"]
shock_names= ['is shocked']
ark_gifs= ["https://media.discordapp.net/attachments/795654835856211990/846798986139664414/Ludociel_using_Ark.gif","https://cdn.discordapp.com/attachments/836293474679783455/847182895243329586/aaaaaaa_6.gif","https://media.discordapp.net/attachments/795654835856211990/846798876983820318/Nerobasta_using_Ark.gif","https://media.discordapp.net/attachments/795654835856211990/846799308970786836/Sariel_and_Tarmiel_using_Omega_Ark.gif"]
ark_names= ['used ark', 'used a powerful attack']



@bot.command(pass_context=True)
async def purge(ctx, limit: int):
 if ctx.author.guild_permissions.manage_messages:
    await ctx.message.delete()
    await ctx.channel.purge(limit=limit)
 else:
            await ctx.send("You cant do that!")


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command()
async def embed(ctx):
    embed=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0xFF5733)
    await ctx.send(embed=embed)


# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="My prefix is Liz/liz", url="http://www.twitch.tv/accountname"))
    print('My Ready is Body')


@bot.listen()
async def on_message(message):
    if "tutorial" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send('This is that you want http://youtube.com/fazttech')
        await bot.process_commands(message)


@bot.command()
async def test(ctx):
    embed=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=discord.Color.blue())
    await ctx.send(embed=embed)

@bot.command()
async def hug (ctx, user: discord.User,name = 'hug', aliases=['HUG']):
 embed = discord.Embed(colour=(discord.Colour.random()), description=f"{ctx.author.mention} {(random.choice(hug_name))} {user.mention}")
 embed.set_image(url=random.choice(hug_gifs))

 await ctx.send(embed=embed)

@bot.command()
async def pat (ctx, user: discord.User,name = 'pat', aliases=['PAT']):
 embed = discord.Embed(colour=(discord.Colour.random()), description=f"{ctx.author.mention} {(random.choice(pat_names))} {user.mention}")
 embed.set_image(url=random.choice(pat_gifs))

 await ctx.send(embed=embed)
 
@bot.command()
async def punch (ctx, user: discord.User,name = 'punch', aliases=['PUNCH']):
 embed = discord.Embed(colour=(discord.Colour.random()), description=f"{ctx.author.mention} {(random.choice(punch_names))} {user.mention}")
 embed.set_image(url=random.choice(punch_gifs))

 await ctx.send(embed=embed)
  
@bot.command()
async def bully (ctx, user: discord.User,name = 'bully', aliases=['BULLY']):
 embed = discord.Embed(colour=(discord.Colour.random()), description=f"{ctx.author.mention} {(random.choice(bully_names))} {user.mention}")
 embed.set_image(url=random.choice(bully_gifs))

 await ctx.send(embed=embed)

@bot.command()
async def kill (ctx, user: discord.User,name = 'kill', aliases=['KILL']):
 embed = discord.Embed(colour=(discord.Colour.random()), description=f"{ctx.author.mention} {(random.choice(kill_names))} {user.mention}")
 embed.set_image(url=random.choice(kill_gifs))

 await ctx.send(embed=embed)

@bot.command()
async def eat (ctx, user: discord.User,name = 'eat', aliases=['EAT']):
 embed = discord.Embed(colour=(discord.Colour.random()), description=f"{ctx.author.mention} {(random.choice(eat_names))} {user.mention}")
 embed.set_image(url=random.choice(eat_gifs))

 await ctx.send(embed=embed)

@bot.command()
async def heal (ctx, user: discord.User,name = 'heal', aliases=['HEAL']):
  embed = discord.Embed(colour=(discord.Colour.random()), description=f"{ctx.author.mention} {(random.choice(heal_names))} {user.mention}")
  embed.set_image(url=random.choice(heal_gifs))

  await ctx.send(embed=embed)

@bot.command()
async def kiss (ctx, user: discord.User,name = 'kiss', aliases=['KISS']):
  embed = discord.Embed(colour=(discord.Colour.random()), description=f"{ctx.author.mention} {(random.choice(kiss_name))} {user.mention}")
  embed.set_image(url=random.choice(kiss_gifs))

  await ctx.send(embed=embed)

@bot.command()
async def help(ctx, args=None):
    help_embed = discord.Embed(title="My Bot's Help!")
    command_names_list = [x.name for x in bot.commands]

    # If there are no arguments, just list the commands:
    if not args:
        help_embed.add_field(
            name="List of commands/info:",
            value="\n".join([str(i+1)+". "+x.name for i,x in enumerate(bot.commands)]),
            inline=False
        )
       
    await ctx.send(embed=help_embed)


@bot.command()
async def happy (ctx,name = 'happy', aliases=['HAPPY']):
  embed = discord.Embed(colour=(discord.Colour.random()), description=f"{ctx.author.mention} {(random.choice(happy_names))}")
  embed.set_image(url=random.choice(happy_gifs))

  await ctx.send(embed=embed)

@bot.command()
async def smile (ctx,name = 'smile', aliases=['SMILE']):
  embed = discord.Embed(colour=(discord.Colour.random()), description=f"{ctx.author.mention} {(random.choice(smile_names))}")
  embed.set_image(url=random.choice(smile_gifs))

  await ctx.send(embed=embed)  


@bot.command()
async def sad (ctx,name = 'sad', aliases=['SAD']):
  embed = discord.Embed(colour=(discord.Colour.random()), description=f"{ctx.author.mention} {(random.choice(sad_names))}")
  embed.set_image(url=random.choice(sad_gifs))

  await ctx.send(embed=embed)

@bot.command()
async def cry (ctx,name = 'cry', aliases=['CRY']):
  embed = discord.Embed(colour=(discord.Colour.random()), description=f"{ctx.author.mention} {(random.choice(cry_names))}")
  embed.set_image(url=random.choice(cry_gifs))

  await ctx.send(embed=embed)  

@bot.command()
async def sleepy (ctx,name = 'sleepy', aliases=['SLEEPY']):
  embed = discord.Embed(colour=(discord.Colour.random()), description=f"{ctx.author.mention} {(random.choice(sleepy_names))}")
  embed.set_image(url=random.choice(sleepy_gifs))

  await ctx.send(embed=embed)  

@bot.command()
async def blush (ctx,name = 'blsuh', aliases=['blush']):
  embed = discord.Embed(colour=(discord.Colour.random()), description=f"{ctx.author.mention} {(random.choice(blush_names))}")
  embed.set_image(url=random.choice(blush_gifs))

  await ctx.send(embed=embed)  

@bot.command()
async def die (ctx,name = 'die', aliases=['DIE']):
  embed = discord.Embed(colour=(discord.Colour.random()), description=f"{ctx.author.mention} {(random.choice(die_names))}")
  embed.set_image(url=random.choice(die_gifs))

  await ctx.send(embed=embed)

@bot.command()
async def shock (ctx,name = 'shock', aliases=['SHOCK']):
  embed = discord.Embed(colour=(discord.Colour.random()), description=f"{ctx.author.mention} {(random.choice(shock_names))}")
  embed.set_image(url=random.choice(shock_gifs))

  await ctx.send(embed=embed)  

@bot.command()
async def ark (ctx,name = 'ark', aliases=['ARK']):
  embed = discord.Embed(colour=(discord.Colour.random()), description=f"{ctx.author.mention} {(random.choice(ark_names))}")
  embed.set_image(url=random.choice(ark_gifs))

  await ctx.send(embed=embed)  

bot.run(os.environ["DISCORD_TOKEN"])