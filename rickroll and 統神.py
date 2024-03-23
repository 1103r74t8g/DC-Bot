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
