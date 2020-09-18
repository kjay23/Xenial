import os
import discord
from discord.ext import commands
from time import sleep
from discord.ext.commands import has_permissions

client = commands.Bot(command_prefix = '>!')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
    activity=discord.Game(f"Type >!help to get the list of commands"))
    print('Xenial Bot is online!')
    
@client.command()
async def ping(ctx):
    await ctx.send(f':ping_pong: | **Pong!** Client Side Ping Latency took {round(client.latency * 1000)}ms!')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.environ['DISCORD_TOKEN'])
