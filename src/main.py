# Import all the necessary dependencies
import disnake
from disnake.ext import commands,tasks
import json

# Load Configuration
config_file = open("./private-config.json")
config = json.loads(config_file.read())
config_file.close()

# Set-Up the bot
intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='t!', intents=intents)

# When the bot is ready this will be executed
@bot.event
async def on_ready():
  print(f"Online on {bot.user}")
  
bot.run(config['token'])