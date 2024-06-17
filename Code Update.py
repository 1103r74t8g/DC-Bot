import asyncio
from http import client
import imp
import resource
from sre_compile import dis
from time import time
import discord
import datetime
import os
import googletrans
from googletrans import Translator
import random
from discord.ext import commands, tasks
from dataclasses import dataclass
from googleapiclient.discovery import build
from discord import app_commands
import requests
import keep_alive



bot_token = ""
channel_ID = 


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)


# 開始運作


@bot.event
async def on_ready():
    channel = bot.get_channel(channel_ID)
    await channel.send("I am so horny")
    # await channel.send(f'{round(bot.latency*1000)} ms')


@bot.command()
async def bobo(ctx):
    url = ["https://imgur.com/lTM93EQ",
           "https://imgur.com/xFPZD05", "https://imgur.com/akST4Vx",
           "https://imgur.com/vNCVD8l", "https://imgur.com/HVYE48w",
           "https://imgur.com/a/67dk26i", "https://imgur.com/DcvugFZ",
           "https://imgur.com/af53IZ8", "https://imgur.com/c69M8DG",
           "https://tenor.com/view/akaonikou-%E8%B5%A4%E9%AC%BC-%E8%B5%A4%E9%AC%BC%E4%BC%AF%E4%BC%AF-%E7%83%82%E7%82%AE%E5%85%B5-%E9%82%B1%E8%90%B1-gif-27458849"]
    random_image_url = random.choice(url)
    await ctx.send(random_image_url)

# 搜尋圖片
api_key = "AIzaSyD7N_dbGR6txYjPJLG0DNIQq-SUfPM2U4Y"


@bot.command()
async def show(ctx, *, search):
    ran = random.randint(0, 9)
    resource = build("customsearch", "v1", developerKey=api_key).cse()
    result = resource.list(
        q=f"{search}", cx="721d7929cf9d249a7", searchType="image").execute()
    url = result["items"][ran]["link"]
    embed1 = discord.Embed(title=f"Here your image ({search.title()})")
    embed1.set_image(url=url)
    await ctx.send(embed=embed1)
# repeat


@bot.command()
async def say(ctx, sb):
    await ctx.send(sb)


# 語音


@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        voice_client = await channel.connect()
        await ctx.send(f'Joined {channel}')
    else:
        await ctx.send('You are not in a voice channel.')

# 音效


@bot.command()
async def sound(ctx):
    voice_channel = ctx.author.voice.channel
    if voice_channel:
        await ctx.send("playing")
        voice_client = await voice_channel.connect()
        audio_source = discord.FFmpegPCMAudio('sound_file.mp3')  # 音效文件的名稱
        voice_client.play(audio_source)
    else:
        await ctx.send("You are not in a voice channel....")
# 翻譯


@bot.command()
async def trans(ctx, lang, *, args):
    a = Translator().translate(args, dest=lang)
    await ctx.send(a.text)

# 回傳


@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} ms')

# 加法


@bot.command()
async def add(ctx, *arr):
    num = 0
    for i in arr:
        num += int(i)
    await ctx.send(f"result = {num}")

# 加減乘除


@bot.command()
async def calculate(ctx, x, w, y):
    if w == "+":
        sum = int(x)+int(y)
    elif w == "-":
        sum = int(x)-int(y)
    elif w == "*":
        sum = int(x)*int(y)
    elif w == "/":
        sum = int(x)/int(y)
    await ctx.send(f"result = {sum}")


# 擲硬幣
@bot.command()
async def coin(ctx):
    await ctx.send('head or tail')

    def check(message):
        return message.author == ctx.author and message.content.lower() in ['head', 'tail']

    response = await bot.wait_for('message', check=check)
    choice = response.content.lower()

    ran = random.choice(['head', 'tail'])
    if choice == ran:
        guess = 'You won!'
    else:
        guess = 'You lost!'

    embed = discord.Embed(
        title="coin <:1013moneyz:1175347212197310524>", description=f"It's {choice}", color=0xfffc41)
    if ran == 'tail':
        embed.set_thumbnail(
            url="https://cdn1-next.cybassets.com/media/W1siZiIsIjU5OTMvcHJvZHVjdHMvMjYzNDc3NjEv5aSn5Y2B5Y676IOMX1NfOTJkZmE5Nzc1ZDMyOTUxM2IyMTIuanBlZyJdLFsicCIsInRodW1iIiwiNjAweDYwMCJdXQ.jpeg?sha=3b871d8564ae6504")
    else:
        embed.set_thumbnail(
            url="https://www.cbc.gov.tw/public/data/issue/money/IMAGES/10_1.jpg")
    embed.add_field(
        name=guess, value=f'the coin is on the {ran} side', inline=False)
    embed.set_image(
        url="https://pic1.zhimg.com/v2-4ac4b8fa74966a153087a4fb00354cd4_b.gif")
    await ctx.send(embed=embed)

# 無聊亂做的


@bot.command()
async def rickroll(ctx):
    embed = discord.Embed(
        title="Never gonna give you up:musical_note:\nNever gonna let you down:musical_note:", color=0x00c7fc)
    embed.set_image(
        url='https://media.tenor.com/x8v1oNUOmg4AAAAd/rickroll-roll.gif')
    await ctx.send(embed=embed)


@bot.command()
async def hotpot(ctx):
    embed = discord.Embed(
        title="啊打 一代一代一代", color=0x00c7fc)
    embed.set_image(
        url='https://media.tenor.com/61yCyJVoyr8AAAAd/桶神-打工.gif')
    await ctx.send(embed=embed)



if(__name__ == "__main__"):
  keep_alive.keep_alive()
  bot.run(bot_token)
