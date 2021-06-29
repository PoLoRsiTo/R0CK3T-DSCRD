import asyncio
from music import music
import discord
from discord.ext import commands
from urllib import parse, request
from discord.utils import get
import re
from random import seed
from random import randint
import random
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
import pytz
import time
import music
from discord import FFmpegPCMAudio
from discord.utils import get


seed(1)

bot=commands.Bot(command_prefix='º', description="This is a discord helper bot")

class DurationConverter(commands.Converter):
    async def convert(self, ctx, argument):
        amount = argument[:-1]
        unit = argument[-1]

        if amount.isdigit() and unit in ['s', 'm']:
            return (int(amount), unit)

        raise commands.BadArgument(message = 'Duración no valida')

@bot.command()

async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def polor(ctx):
    await ctx.send('la vaaaca looola')

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall( r"watch\?v=(\S{11})", html_content.read().decode())
    print(search_results)
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

@bot.command()
async def tula(ctx, member: discord.Member):
    for _ in range(10):
        value = randint(0, 12)
        print(value)
    contestaciones = ['cm, buena tula bro', 'cm de puro placer', 'cm de ariete', 'cm, enhorabuena manin', 'cm de perforadora', 'cm, eres mostopapi?']
    await ctx.send(f'{member.mention}' + " " + 'tiene' + ' ' + str(value) + random.choice(contestaciones))

@bot.command()
async def avatar(ctx, member: discord.Member):
    await ctx.send('{}'.format(member.avatar_url))

@commands.has_permissions(kick_members=True)
@bot.command()
async def kickear(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} kickeado por' + reason)

@bot.command()
async def banear(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} baneado por' + reason)

@bot.command()
async def god(ctx, member: commands.MemberConverter, duration: DurationConverter):

    multiplier = {'s': 1, 'm': 60}
    amount, unit = duration


    await ctx.guild.ban(member)
    await ctx.send(f'Troleador bot')
    await asyncio.sleep(amount * multiplier[unit])
    await ctx.guild.unban(member)

@bot.command()
async def desbanear(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} ha sido desbaneado')
            return

@bot.command()
async def nomeseloscomandos(ctx):
    lista_comandos = ["tula: Te digo cuanto te mide a tí o a quién menciones.", "kickear: Solo el SiLLoW y Admins", "banear: Lo mismo pero con baneo.", "avatar: Te envio el avatar de quién menciones.", "ping: Te respondo pong.", "youtube: Te envio el primer resultado de lo que pongas en youtube.", "polor: La vaaca Looola.", "tivu_yamchi_garbans: Oniichan."]
    await ctx.send(lista_comandos)

@bot.command()
async def bitcoin(ctx):
    url = 'https://es.investing.com/crypto/bitcoin'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    it = soup.find_all("span", {"id": "last_last"})

    items = list()

    for i in it:
        items.append(i.text)
    
    coins = str(items)

    await ctx.send(coins)

@bot.command()
async def tivu_yamchi_garbans(ctx):
    await ctx.send("onii-chan uwu ✨✨")

@bot.command()
async def enviar(ctx, arg1, *, arg2):
    canal = discord.utils.get(ctx.guild.channels, name=arg1)
    await canal.send(arg2)

@bot.command()
async def anuncio(ctx, arg1, arg2, arg3, arg4, *, arg5):
    canal = discord.utils.get(ctx.guild.channels, name=arg1)
    hora_peninsular = pytz.timezone('Europe/Madrid')
    hora = datetime.now(hora_peninsular)
    d = int(arg2) - (hora.day)
    h = int(arg3) - (hora.hour)
    m = int(arg4) - (hora.minute)
    mi = m

    if "-" in str(m):
        mi = m*(-1)
    else:
        print("no")
    DD = d*86400
    MM = mi*60
    HH = h*3600
    secs = MM + HH + DD
    time.sleep(secs)
    await canal.send(arg5)

@bot.command(name='hablar',
    description='Talk',
    pass_context=True,)
async def hablar(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    source = FFmpegPCMAudio('talking2.mp3')
    player = voice.play(source)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="este server"))
    print("My bot is ready")

@bot.event
async def on_member_join(ctx, member):
    print(f'{member} se ha vuelto Trolo')
    ctx.send(f'{member} dejó de ser ReTrol')

@bot.event
async def on_member_remove(ctx, member):
    print(f'{member} dejó de ser ReTrol')
    ctx.send(f'{member} dejó de ser ReTrol')

cogs = [music]

for i in range(len(cogs)):
    cogs[i].setup(bot)

bot.run('NzQzNDc5NzMzMDI2ODE2MTMx.XzVRdQ.69iZ48_saxGFlHZID2zlr-3C1Ds')
