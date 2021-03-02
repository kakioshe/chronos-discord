import os
from dotenv import load_dotenv
from discord.ext import commands
from discord import User, TextChannel

client = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
  
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await client.process_commands(message)
    
@client.command()
async def ping(ctx, channel: TextChannel, user: User, *, message=""):
    await channel.send(f"{ctx.author.mention}: {message} {user.mention}")

load_dotenv()
client.run(os.getenv('TOKEN'))