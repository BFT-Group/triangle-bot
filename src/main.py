import os
import disnake
from disnake.ext import commands,tasks
import time

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='t!', intents=intents)


@bot.event
async def on_ready():
  print(f"Online on {bot.user}")
  

bot.run(os.environ['token'])