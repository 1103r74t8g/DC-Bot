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
