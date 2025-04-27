import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
bot = commands.Bot(command_prefix=':', intents=intents)
bot.remove_command('help')

# Cargar cogs
@bot.event
async def on_ready():
    print(f'Conectado como {bot.user}')
    for filename in os.listdir('./src/cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'Cog {filename} cargado.')
            except Exception as e:
                print(f'Error al cargar {filename}: {e}')

@bot.event
async def on_disconnect():
    print('Desconectado del servidor.')

if __name__ == '__main__':
    bot.run(TOKEN)