import os
import nacl
import asyncio
import discord
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())
class NotConnectedError(Exception):
    "Raised when not connected to voice channel"
    pass


@bot.command()
async def ping(context):
  await context.send(f"Pong! Latency is {bot.latency*1000:.3f}ms")


@bot.command(name = "join", help = "use your fucking eyes")
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
        if not ctx.message.guild.voice_client is None:
            await ctx.send("I am already connected to a voice channel!")
        else:
            await channel.connect()
        return


@bot.command(name = "leave", help = "use your fucking eyes")
async def leave(ctx):
    try:
        channel = ctx.message.guild.voice_client
        if channel is None:
            raise NotConnectedError
        await channel.disconnect()
    except NotConnectedError:
        await ctx.send("I am not currently connected to any channel!")
    return

@bot.event
async def on_ready():
    print("working and online!")

# @bot.event
# async def on_message(message):
#    await bot.process_commands(message)
#    if (message.author.global_name == "datderps" or message.author.global_name == "derpflections") and message.channel.id == 1145004637515173949: 
#         print(message)
#         await message.channel.send(message.content)


token = os.getenv('token')
bot.run(token)
