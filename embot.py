# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

#Environmental Variables
load_dotenv()
TOKEN = os.environ.get('DISCORD_TOKEN')
GUILD = os.environ.get('DISCORD_GUILD')
CHANNEL = os.environ.get('DISCORD_CHANNEL')
emulatorurl = os.environ.get('URL')

bot = commands.Bot(command_prefix='!')

#Triggers when the Bot is connected
@bot.event
async def on_ready():
    global guild 
    global beeroom
    global strikes
    
    guild = discord.utils.get(bot.guilds, name = GUILD)
    beeroom = discord.utils.get(guild.text_channels, name = 'beeroom')
    strikes = discord.utils.get(guild.text_channels, name = 'strikes')
    embulator = discord.utils.get(guild.text_channels, name = 'embulator')

    #Print out the guild and guild id
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    print(bot.guilds)

#load extensions
@bot.command()
async def load(extension_name :str):
    bot.load_extension(extension_name)
    await bot.say("Extension Loaded")

#load cogs, run bot.
if __name__ == "__main__":
    bot.load_extension("cogs.strikecog")
bot.run(TOKEN)
