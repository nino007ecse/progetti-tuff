import discord
from discord.ext import commands
import asyncio
import aiohttp

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=';', intents=intents)

webhooks = []
messages = []
waiting_for_webhooks = False
waiting_for_messages = False
current_user = None
raid_webhooks = []
raid_messages = []
waiting_for_raid_message = False
waiting_for_raid_confirm = False
raid_user = None
raid_message_content = None
spam_webhook_url = None
spam_message = None
waiting_for_spam_url = False
waiting_for_spam_message = False
spam_user = None
waiting_for_spam_confirm = False

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command(name='dm')
async def dm(ctx, *, message):
    if not ctx.author.guild_permissions.manage_roles:
        return
    
    if not ctx.guild:
        return
    
    members = ctx.guild.members
    
    for member in members:
        if member.bot:
            continue
        
        try:
            await member.send(message)
            await asyncio.sleep(0.5)
        except:
            pass
    
    await ctx.send('-# 👍')

@bot.group(name='webhook', aliases=['wh'])
async def webhook(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('-# Available commands: ;webhook send, ;webhook create, ;webhook raid, ;webhook spam')

@webhook.command(name='send')
async def webhook_send(ctx):
    global webhooks, messages, waiting_for_webhooks, waiting_for_messages, current_user
    
    if not ctx.author.guild_permissions.manage_webhooks:
        return
    
    webhooks = []
    messages = []
    waiting_for_webhooks = True
    waiting_for_messages = False
    current_user = ctx.author.id
    
    await ctx.send('-# Send webhook URLs (one per line, type "done" when finished):')

@webhook.command(name='create')
async def webhook_create(ctx, *, name='Webhook'):
    if not ctx.author.guild_permissions.manage_webhooks:
        return
    
    if not ctx.guild:
        return
    
    try:
        webhook = await ctx.channel.create_webhook(name=name)
        await ctx.send(f'-# {webhook.url}')
        await ctx.send('-# 👍')
    except:
        return

@webhook.command(name='raid')
async def webhook_raid(ctx):
    global waiting_for_raid_message, raid_user
    
    if not ctx.author.guild_permissions.manage_webhooks:
        return
    
    if not ctx.guild:
        return
    
    embed = discord.Embed(
        title='wh raid',
        description='type ur message in chat',
        color=0x2b2d31
    )
    
    await ctx.send(embed=embed)
    
    waiting_for_raid_message = True
    raid_user = ctx.author.id

@webhook.command(name='spam')
async def webhook_spam(ctx):
    global waiting_for_spam_url, spam_user
    
    if not ctx.author.guild_permissions.manage_webhooks:
        return
    
    if not ctx.guild:
        return
    
    await ctx.send('-# Send webhook URL:')
    
    waiting_for_spam_url = True
    spam_user = ctx.author.id

@bot.event
async def on_message(message):
    global webhooks, messages, waiting_for_webhooks, waiting_for_messages, current_user
    global raid_webhooks, raid_messages, waiting_for_raid_message, raid_user, waiting_for_raid_confirm, raid_message_content
    global spam_webhook_url, spam_message, waiting_for_spam_url, waiting_for_spam_message, spam_user, waiting_for_spam_confirm
    
    if message.author == bot.user:
        return
    
    if waiting_for_spam_url and message.author.id == spam_user:
        waiting_for_spam_url = False
        spam_webhook_url = message.content.strip()
        await message.channel.send('-# Send message to spam:')
        waiting_for_spam_message = True
        await message.channel.send('-# 👍')
        return
    
    if waiting_for_spam_message and message.author.id == spam_user:
        waiting_for_spam_message = False
        spam_message = message.content
        await message.channel.send('-# **:**')
        waiting_for_spam_confirm = True
        return
    
    if waiting_for_spam_confirm and message.author.id == spam_user:
        waiting_for_spam_confirm = False
        
        if message.content.lower() == 'y':
            await message.channel.send('-# Spamming...')
            
            async with aiohttp.ClientSession() as session:
                for _ in range(50):
                    try:
                        async with session.post(spam_webhook_url, json={'content': spam_message}) as resp:
                            if resp.status == 429:
                                await asyncio.sleep(2)
                                continue
                    except:
                        pass
                    await asyncio.sleep(0.5)
            
            await message.channel.send('-# 👍')
        else:
            await message.channel.send('-# Spam cancelled')
        
        spam_webhook_url = None
        spam_message = None
        return
    
    if waiting_for_raid_message and message.author.id == raid_user:
        waiting_for_raid_message = False
        raid_message_content = message.content
        
        await message.channel.send('-# **:**')
        waiting_for_raid_confirm = True
        return
    
    if waiting_for_raid_confirm and message.author.id == raid_user:
        waiting_for_raid_confirm = False
        
        if message.content.lower() == 'y':
            embed = discord.Embed(
                title='wh raid',
                description='creating and sending wh',
                color=0x2b2d31
            )
            await message.channel.send(embed=embed)
            
            created_webhooks = []
            for i in range(10):
                try:
                    webhook = await message.channel.create_webhook(name=f'Raid-{i+1}')
                    created_webhooks.append(webhook.url)
                    await asyncio.sleep(1.5)
                except discord.HTTPException as e:
                    if e.status == 429:
                        await asyncio.sleep(5)
                        continue
                    break
                except:
                    pass
            
            async with aiohttp.ClientSession() as session:
                for webhook_url in created_webhooks:
                    for _ in range(8):
                        try:
                            async with session.post(webhook_url, json={'content': raid_message_content}) as resp:
                                if resp.status == 429:
                                    await asyncio.sleep(2)
                                    continue
                        except:
                            pass
                        await asyncio.sleep(0.8)
            
            embed = discord.Embed(
                title='wh raid',
                description='creating and sending wh',
                color=0x2b2d31
            )
            await message.channel.send(embed=embed)
            await message.channel.send('-# 👍')
            
            for webhook_url in created_webhooks:
                try:
                    async with aiohttp.ClientSession() as session:
                        await session.delete(webhook_url)
                except:
                    pass
            
        else:
            embed = discord.Embed(
                title='wh raid',
                description='raid cancelled >_<',
                color=0x2b2d31
            )
            await message.channel.send(embed=embed)
        
        raid_webhooks = []
        raid_messages = []
        raid_message_content = None
        return
    
    if waiting_for_webhooks and message.author.id == current_user:
        if message.content.lower() == 'done':
            waiting_for_webhooks = False
            waiting_for_messages = True
            await message.channel.send(f'-# Received {len(webhooks)} webhook(s). Send messages (one per line, type "done" when finished):')
            await message.channel.send('-# 👍')
            return
        
        webhooks.append(message.content.strip())
        await message.channel.send('-# 👍')
        return
    
    if waiting_for_messages and message.author.id == current_user:
        if message.content.lower() == 'done':
            waiting_for_messages = False
            await message.channel.send(f'-# Sending to {len(webhooks)} webhook(s)...')
            
            async with aiohttp.ClientSession() as session:
                for webhook_url in webhooks:
                    for msg in messages:
                        try:
                            async with session.post(webhook_url, json={'content': msg}) as resp:
                                if resp.status == 429:
                                    await asyncio.sleep(2)
                                    continue
                        except:
                            pass
                        await asyncio.sleep(0.5)
            
            await message.channel.send('-# 👍')
            webhooks = []
            messages = []
            return
        
        messages.append(message.content)
        await message.channel.send('-# 👍')
        return
    
    await bot.process_commands(message)

bot.run('TOKEN NEGRACCI')
