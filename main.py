import asyncio
import datetime
import discord
import requests
import json
import random
import youtube_dl
from discord.ext import commands, tasks
import discord.utils

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)

target_channel_id = 743776019911278655

idchannel = 750446189119537233


@tasks.loop(hours=24)
async def called_once_a_day():
    message_channel = bot.get_channel(target_channel_id)
    print(f"Mesaj trimis in {message_channel}")
    await message_channel.send(random.choice(mesaje_repetate))


@called_once_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("Mesaj trimis!")


called_once_a_day.start()

glume = [
    "```exemplu```",
]


@tasks.loop(hours=4)
async def called_once_a_day():
    message_channel = bot.get_channel(target_channel_id)
    print(f"Mesaj trimis in {message_channel}")
    await message_channel.send(random.choice(glume))


@called_once_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("Mesaj trimis!")


called_once_a_day.start()

starter_encouragements = [
    "exemplu",
]

mesaje_repetate = [
    "```exemplu```",

]

smecherii_de_raspuns = [
    "exemplu",
    "exemplu",
]

best_page = [
    "exemplu",
]


comenzi = """
```
exemplu

```
"""


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return quote


voice_clients = {}

yt_dl_opts = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

ffmpeg_options = {'options': "-vn"}


@bot.event
async def on_message(msg):
    if msg.content.startswith("$play"):

        try:
            voice_client = await msg.author.voice.channel.connect()
            voice_clients[voice_client.guild.id] = voice_client

        except:
            print("error")

        try:
            url = msg.content.split()[1]

            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

            song = data['url']
            player = discord.FFmpegPCMAudio(song, **ffmpeg_options)

            voice_clients[msg.guild.id].play(player)

        except Exception as err:
            print(err)

    if msg.content.startswith("$pause"):
        try:
            voice_clients[msg.guild.id].pause()
        except Exception as err:
            print(err)

    if msg.content.startswith("$resume"):
        try:
            voice_clients[msg.guild.id].resume()
        except Exception as err:
            print(err)

    if msg.content.startswith("$stop"):
        try:
            voice_clients[msg.guild.id].stop()
            await voice_clients[msg.guild.id].disconnect()
        except Exception as err:
            print(err)


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(idchannel)
    embed = discord.Embed(title="Oho!", description=f"{member.mention} tocmai a intrat 🥰")
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)
    role = discord.utils.get(member.guild.roles, id=780384577914929153)
    await member.add_roles(role)


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(idchannel)
    embed = discord.Embed(title=f"Sa-mi bag...", description=f"{member.mention} tocmai a iesit 😐")
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("$help pentru comenzi"))
    print('logat prin {0.user}'.format(bot))


@bot.command()
async def image(ctx):
    embed = discord.Embed(title="Random Image",
                          colour=discord.Colour(0x7289DA),
                          description=f"Random Image",
                          timestamp=datetime.datetime.utcfromtimestamp(1580842764))
    embed.set_image(url=(random.choice(images)))
    await ctx.send(embed=embed)


@bot.event
async def on_message(message):
    if message.content.startswith("$play"):

        try:
            voice_client = await message.author.voice.channel.connect()
            voice_clients[voice_client.guild.id] = voice_client
        except:
            print("error")

        try:
            url = message.content.split()[1]

            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

            song = data['url']
            player = discord.FFmpegPCMAudio(song, **ffmpeg_options)

            voice_clients[message.guild.id].play(player)

        except Exception as err:
            print(err)

    if message.content.startswith("$pause"):
        try:
            voice_clients[message.guild.id].pause()
        except Exception as err:
            print(err)

    if message.content.startswith("$resume"):
        try:
            voice_clients[message.guild.id].resume()
        except Exception as err:
            print(err)

    if message.content.startswith("$stop"):
        try:
            voice_clients[message.guild.id].stop()
            await voice_clients[message.guild.id].disconnect()
        except Exception as err:
            print(err)

    if message.author == bot.user:
        return

    if message.content.startswith('exemplu'):
        await message.channel.send('exemplu')

    if message.content.startswith('exemplu'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('exemplu'):
        await message.channel.send(random.choice(starter_encouragements))

    if message.content.startswith('exemplu'):
        await message.channel.send(random.choice(smecherii_de_raspuns))

    if message.content.startswith('exemplu'):
        await message.channel.send(random.choice(gangsta))

    if message.content.startswith('exemplu'):
        await message.channel.send(random.choice(best_page))

    if message.content.startswith('exemplu'):
        await message.channel.send(comenzi)

    if message.content.startswith('exemplu'):
        with open('exemplu.jpg', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)

bot.run('token')
