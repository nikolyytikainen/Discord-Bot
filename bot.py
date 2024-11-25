import discord
from discord.ext import commands
from Responses import register_commands
from dotenv import load_dotenv
import os

# Lataa .env-tiedoston muuttujat
load_dotenv()
dcToken = os.getenv('discordToken')


# Botin intentsit ja alustaminen
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Eventi botin valmiustilan tarkistamiseen
@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')

# Eventi viestien käsittelyyn
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    user_message = str(message.content)
    if user_message.startswith('!'):
        await bot.process_commands(message)  # Käsittelee komennot
    
        
# Rekisteröi komennot responses.py:stä
register_commands(bot)

# Käynnistää botin
bot.run(dcToken)
