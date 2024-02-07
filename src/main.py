import disnake
from disnake.ext import commands,tasks
import json
import random
import sys
import os
import requests
import time


config_file = open("./private-config.json")
config = json.loads(config_file.read())
config_file.close()

class Triangle:
  instance_type = "Local"
  actions_hour_loops = 0
  last_hourly_triangle = ""
  github_token = ""
  job_url = ""

triangle_bot = Triangle()

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='t!', intents=intents)

def posting_format_name(triangle: str):
  dotindex = triangle.find(".")
  triangle = triangle[:dotindex]
  triangle = triangle.replace("-"," ")
  last_was_space = False
  formatted = ""
  index = 1
  for char in triangle:
    if last_was_space:
      new_char = char.upper()
      last_was_space = False
    elif index == 1:
      new_char = char.upper()
    else:
      new_char = char
    formatted = formatted + new_char
    if char == " ":
      last_was_space = True
    index += 1
  print(formatted)
  return formatted

@tasks.loop(hours=1)
async def triangle_posting():
  posting_channel = await bot.fetch_channel(1106596947923583037)
  await posting_channel.send(content="# Triangle bot is shutting down..\n## Why?\nI haven't been working on it for a while and it's not really needed anymore.\n## When?\nNow.\n## Thank you.\n```\nThanks:\n\nRuudie\nBaskoot\n```\n\n Developed by: cdc | Goodbye!")
  return
  files = os.listdir("./resources/images/triangle-posting/")
  retries = 0
  triangle = random.choice(files)
  while (triangle == triangle_bot.last_hourly_triangle):
    triangle = random.choice(files)
    retries += 1
  triangle_bot.last_hourly_triangle = triangle
  await posting_channel.send(content=f"This hour's triangle is: **{posting_format_name(str(triangle))}**\n\nI had to reroll {retries} times",file=disnake.File(f"./resources/images/triangle-posting/{triangle}"))


@tasks.loop(hours=5,minutes=59)
async def actions_restart_bot():
  if triangle_bot.actions_hour_loops > 0:
    info_channel = await bot.fetch_channel(1026074277432283186)
    await info_channel.send("`🚨 OUTAGE ALERT 🚨` Step Runtime Limit Reached! Restarting the Bot.")
    await info_channel.send("The bot should be back in 3 minutes or less.")
    os.system("gh workflow run discord-bot.yml --ref main")
    await bot.close()
  triangle_bot.actions_hour_loops += 1
  info_channel = await bot.fetch_channel(1026074277432283186)
  await info_channel.send(f"`✔ ACTIONS FAIL PREVENTION ✔` 5:59:00 Countdown Started!")

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
    actions_restart_bot.start()
    triangle_bot.github_token = sys.argv[3]
    triangle_bot.job_url = open("./actions_job_id.txt").read()
  await bot.change_presence(activity=disnake.Game(name=f"{bot.command_prefix}help{commitstring}"))
  info_channel = await bot.fetch_channel(1026074277432283186)
  await info_channel.send(f"`🤖 BOOTED UP 🤖` Successfully started and online! Running on `{triangle_bot.instance_type}`!")
  triangle_posting.start()
  
bot.run(config['token'])
