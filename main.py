import os
import time
import asyncio
import pytz
from dotenv import load_dotenv
from discord.ext import commands
from discord import User, TextChannel, Role
from datetime import datetime

load_dotenv()

CHANNEL_ID = int(os.getenv('CHANNEL_ID'))
GUILD_ID = int(os.getenv('GUILD_ID'))
ROLE_ID = int(os.getenv('ROLE_ID'))

client = commands.Bot(command_prefix="$")
server_timezone = pytz.timezone("Asia/Jakarta")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await sendReminder()
  
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await client.process_commands(message)
    
@client.command()
async def ping(ctx, channel: TextChannel, user: User, *, message=""):
    await channel.send(f"{ctx.author.mention}: {message} {user.mention}")

async def sendReminder():
    print("Test")
    while(True):
        if (datetime.now(server_timezone).hour == 13):
            channel = client.get_channel(CHANNEL_ID)
            guild = client.get_guild(GUILD_ID)
            print(guild)
            if guild:
                role = guild.get_role(ROLE_ID)
                await channel.send(f"Daily hoyoLab {role.mention}")
            else:
                return
        await asyncio.sleep(3600)
    

client.run(os.getenv('TOKEN'))