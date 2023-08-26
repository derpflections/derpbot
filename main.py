import os
import discord
from dotenv import load_dotenv
load_dotenv()

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("online")

@client.event
async def on_message(message):
    if message.author != client.user:
        await message.channel.send(message.content[::1])

token = os.getenv('token')
client.run(token)