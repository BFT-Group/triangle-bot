import disnake
from disnake.ext import commands,tasks
import json

config_file = open("./private-config.json")
config = json.loads(config_file.read())
config_file.close()

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='t!', intents=intents)

@bot.slash_command()
async def kill(inter):
  await inter.send("Killing")
  quit()

@bot.command()
async def ping(ctx):
  await ctx.reply("pong")
@bot.event
async def on_ready():
  print(f"Online on {bot.user}")
  
bot.run(config['token'])