# Import all the necessary dependencies
import disnake
from disnake.ext import commands,tasks

# Set-Up the bot
intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='t!', intents=intents)

# When the bot will be ready print into console
@bot.event
async def on_ready():
  print(f"Online on {bot.user}")
  
#bot.run(os.environ['token'])