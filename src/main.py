import disnake
from disnake.ext import commands,tasks
import json
import random
import sys

config_file = open("./private-config.json")
config = json.loads(config_file.read())
config_file.close()

class Triangle:
  instance_type = "Local"
  actions_hour_loops = 0

triangle_bot = Triangle()

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='t!', intents=intents)

@tasks.loop(hours=5,minutes=59)
async def actions_restart_bot():
  if triangle_bot.actions_hour_loops > 0:
    info_channel = await bot.fetch_channel(1026074277432283186)
    await info_channel.send("`🚨 OUTAGE ALERT 🚨` Step Runtime Limit Reached! Shutting Down.")
    print("Step Limit Reached")
    print("Shutting Down To Prevent Failure")
    await bot.close()
  triangle_bot.actions_hour_loops += 1

@bot.slash_command()
async def triangle(inter):
  """What Triangle Are you"""
  choices = ["Nerd","Awesome","Unibrow","Programmer","King"]
  await inter.send(f"You are {random.choice(choices)} Triangle! Amazing!")

@bot.slash_command()
async def kill(inter):
  if inter.author.id != 708750647847157880:
    await inter.send("Are you cdc? No? Ok then! I'm not shutting down lol")
    print("--- WARNING ---")
    print(f"{inter.author} tried to kill {bot.user}")
    print("---         ---")
    return
  await inter.send("Killing")
  await bot.close()


@bot.event
async def on_ready():
  print(f"Online on {bot.user}")
  commitstring = ""
  try:
    if sys.argv[1] != None:
      commit = sys.argv[1][:7]
      summary = sys.argv[2]
      if summary != "":
        commitstring = f" [{commit}] ({summary})"
      else:
        commitstring = f" [{commit}]"
  except:
    print("Running Locally")
  else:
    print("Running On Actions")
    triangle_bot.instance_type = "Actions"
  await bot.change_presence(activity=disnake.Game(name=f"{bot.command_prefix}help{commitstring}"))
  
bot.run(config['token'])