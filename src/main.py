import disnake
from disnake.ext import commands,tasks
import json

config_file = open("./private-config.json")
config = json.loads(config_file.read())
config_file.close()

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='t!', intents=intents)


@bot.event
async def on_message(m):
  if m.author.bot:
    return
  if m.content.find("circle") >= 0:
    await m.channel.send("ew i hate that guy.")
    await m.delete()
    

@bot.slash_command()
async def kill(inter):
  await inter.send("Killing")
  await bot.close()

@bot.command()
async def ping(ctx):
  await ctx.reply("pong")

@bot.event
async def on_ready():
  print(f"Online on {bot.user}")
  
bot.run(config['token'])