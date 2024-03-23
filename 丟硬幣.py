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
