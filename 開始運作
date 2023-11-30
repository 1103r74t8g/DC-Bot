@bot.event
async def on_ready():
    channel = bot.get_channel(channel_ID)
    await channel.send("hello,Im ready")
    await channel.send(f'{round(bot.latency*1000)} ms')
