@bot.command()
async def trans(ctx, lang, *, args):
    a = Translator().translate(args, dest=lang)
    await ctx.send(a.text)
