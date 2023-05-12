import disnake
from disnake.ext import commands,tasks
import json
import random
import sys

config_file = open("./private-config.json")
config = json.loads(config_file.read())
config_file.close()

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='t!', intents=intents)



@bot.slash_command()
async def triangle(inter):
  """What Triangle Are you"""
  choices = ["Nerd","Awesome","Unibrow","Programmer","King"]
  await inter.send(f"You are {random.choice(choices)} Triangle! Amazing!")

@bot.slash_command()
async def kill(inter):
  if inter.author.id != 708750647847157880:
    await inter.send("Are you cdc? No? Ok then! I'm not shutting down lol")
    return
  await inter.send("Killing")
  await bot.close()

@bot.command()
async def ping(ctx):
  await ctx.reply("pong")

@bot.event
async def on_ready():
  print(f"Online on {bot.user}")
  commitstring = ""
  if sys.argv[1] != None:
    commit = sys.argv[1][:7]
    summary = sys.argv[2]
    commitstring = f" [{commit}] ({summary})"
  await bot.change_presence(activity=disnake.Game(name=f"{bot.command_prefix}help{commitstring}"))
  
bot.run(config['token'])