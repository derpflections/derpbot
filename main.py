import os
import discord

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("online")

@client.event
async def on_message(message):
    if message.author != client.user:
        await message.channel.send(message.content[::1])

token = "MTE0NDg4MjYyMDE1NzY2MTI4NQ.GbTvNt.hlsQzk9F6faYi4WSjQxytI7bBB6BUH6u0JQmA8"
client.run(token)