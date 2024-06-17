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
