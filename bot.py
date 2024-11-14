import discord
from discord.ext import commands
import os

# Создаем объект бота
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Подключаем команды из папки commands
async def load_commands():
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            await bot.load_extension(f"commands.{filename[:-3]}")

# Событие запуска бота
@bot.event
async def on_ready():
    print(f"Бот {bot.user} готов!")
    await load_commands()  # Загружаем команды из папки commands
    try:
        synced = await bot.tree.sync()
        print(f"Синхронизировано {len(synced)} команд.")
    except Exception as e:
        print(f"Ошибка при синхронизации команд: {e}")

# Запуск бота с вашим токеном
bot.run("TOKEN")
