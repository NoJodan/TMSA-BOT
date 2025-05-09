import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from database.mongo_manager import MongoManager  # Importar MongoManager

# Cargar variables de entorno
load_dotenv()

# Obtener valores del archivo .env
TOKEN = os.getenv('DISCORD_TOKEN')
MONGODB_URL = os.getenv('MONGODB_URL')
MONGODB_DB_NAME = os.getenv('MONGODB_DB_NAME')

# Validar que las variables de entorno estén definidas
if not MONGODB_URL:
    raise ValueError("La URI de MongoDB (MONGODB_URL) no está definida en el archivo .env")
if not MONGODB_DB_NAME:
    raise ValueError("El nombre de la base de datos (MONGODB_DB_NAME) no está definido en el archivo .env")

# Crear la instancia de MongoManager
mongo_manager = MongoManager(MONGODB_URL, MONGODB_DB_NAME)
mongo_manager.connect()

# Configurar intents y crear el bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)
bot.remove_command('help')

@bot.command(name='ping', description='Responde con pong!')
async def ping(ctx):
    await ctx.send('pong!')

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
    
    try:
        await bot.tree.sync()
        print('Sincronización de comandos completada.')
    except Exception as e:
        print(f'Error al sincronizar comandos: {e}')

@bot.event
async def on_disconnect():
    print('Desconectado del servidor.')
    mongo_manager.close()

if __name__ == '__main__':
    bot.mongo_manager = mongo_manager.database
    bot.run(TOKEN)