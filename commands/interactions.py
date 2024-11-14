import discord
from discord import app_commands
from discord.ext import commands
import requests

NEKOS_API_URL = "https://nekos.best/api/v2"

# Функция для получения гифки из Nekos API
def get_gif(action):
    response = requests.get(f"{NEKOS_API_URL}/{action}")
    if response.status_code == 200:
        data = response.json()
        return data["results"][0]["url"]
    return None

class InteractionCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Команда для объятий
    @app_commands.command(name="hug", description="Обнять пользователя")
    async def hug(self, interaction: discord.Interaction, member: discord.Member):
        gif_url = get_gif("hug")
        if gif_url:
            await interaction.response.send_message(
                f"{interaction.user.mention} обнимает {member.mention} 🤗", 
                embed=discord.Embed().set_image(url=gif_url)
            )
        else:
            await interaction.response.send_message("Не удалось получить гифку.")

    # Команда для поцелуев
    @app_commands.command(name="kiss", description="Поцеловать пользователя")
    async def kiss(self, interaction: discord.Interaction, member: discord.Member):
        gif_url = get_gif("kiss")
        if gif_url:
            await interaction.response.send_message(
                f"{interaction.user.mention} целует {member.mention} 😘", 
                embed=discord.Embed().set_image(url=gif_url)
            )
        else:
            await interaction.response.send_message("Не удалось получить гифку.")
    
    # Команда для поглаживания
    @app_commands.command(name="pat", description="Погладить пользователя")
    async def pat(self, interaction: discord.Interaction, member: discord.Member):
        gif_url = get_gif("pat")
        if gif_url:
            await interaction.response.send_message(
                f"{interaction.user.mention} гладит {member.mention} 😊", 
                embed=discord.Embed().set_image(url=gif_url)
            )
        else:
            await interaction.response.send_message("Не удалось получить гифку.")

    # Команда для крепких объятий
    @app_commands.command(name="cuddle", description="Обнять крепко пользователя")
    async def cuddle(self, interaction: discord.Interaction, member: discord.Member):
        gif_url = get_gif("cuddle")
        if gif_url:
            await interaction.response.send_message(
                f"{interaction.user.mention} крепко обнимает {member.mention} 🫂", 
                embed=discord.Embed().set_image(url=gif_url)
            )
        else:
            await interaction.response.send_message("Не удалось получить гифку.")

    # Команда для щекотки
    @app_commands.command(name="tickle", description="Пощекотать пользователя")
    async def tickle(self, interaction: discord.Interaction, member: discord.Member):
        gif_url = get_gif("tickle")
        if gif_url:
            await interaction.response.send_message(
                f"{interaction.user.mention} щекочет {member.mention} 😂", 
                embed=discord.Embed().set_image(url=gif_url)
            )
        else:
            await interaction.response.send_message("Не удалось получить гифку.")

    # Команда для пощечины
    @app_commands.command(name="slap", description="Дать пощечину пользователю")
    async def slap(self, interaction: discord.Interaction, member: discord.Member):
        gif_url = get_gif("slap")
        if gif_url:
            await interaction.response.send_message(
                f"{interaction.user.mention} дает пощечину {member.mention} 👋", 
                embed=discord.Embed().set_image(url=gif_url)
            )
        else:
            await interaction.response.send_message("Не удалось получить гифку.")

    # Команда для укусов
    @app_commands.command(name="bite", description="Укусить пользователя")
    async def bite(self, interaction: discord.Interaction, member: discord.Member):
        gif_url = get_gif("bite")
        if gif_url:
            await interaction.response.send_message(
                f"{interaction.user.mention} кусает {member.mention} 🐾", 
                embed=discord.Embed().set_image(url=gif_url)
            )
        else:
            await interaction.response.send_message("Не удалось получить гифку.")

    # Команда для кормления
    @app_commands.command(name="feed", description="Покормить пользователя")
    async def feed(self, interaction: discord.Interaction, member: discord.Member):
        gif_url = get_gif("feed")
        if gif_url:
            await interaction.response.send_message(
                f"{interaction.user.mention} кормит {member.mention} 🍙", 
                embed=discord.Embed().set_image(url=gif_url)
            )
        else:
            await interaction.response.send_message("Не удалось получить гифку.")

    # Команда для самодовольной улыбки
    @app_commands.command(name="smug", description="Самодовольно улыбнуться пользователю")
    async def smug(self, interaction: discord.Interaction, member: discord.Member):
        gif_url = get_gif("smug")
        if gif_url:
            await interaction.response.send_message(
                f"{interaction.user.mention} самодовольно улыбается {member.mention} 😏", 
                embed=discord.Embed().set_image(url=gif_url)
            )
        else:
            await interaction.response.send_message("Не удалось получить гифку.")

    # Команда для тычков
    @app_commands.command(name="poke", description="Ткнуть пользователя")
    async def poke(self, interaction: discord.Interaction, member: discord.Member):
        gif_url = get_gif("poke")
        if gif_url:
            await interaction.response.send_message(
                f"{interaction.user.mention} тычет {member.mention} 👉", 
                embed=discord.Embed().set_image(url=gif_url)
            )
        else:
            await interaction.response.send_message("Не удалось получить гифку.")

    # Команда для пяти
    @app_commands.command(name="highfive", description="Дать пять пользователю")
    async def highfive(self, interaction: discord.Interaction, member: discord.Member):
        gif_url = get_gif("highfive")
        if gif_url:
            await interaction.response.send_message(
                f"{interaction.user.mention} дает пять {member.mention} 🙌", 
                embed=discord.Embed().set_image(url=gif_url)
            )
        else:
            await interaction.response.send_message("Не удалось получить гифку.")

    # Команда для махания рукой
    @app_commands.command(name="wave", description="Помахать пользователю")
    async def wave(self, interaction: discord.Interaction, member: discord.Member):
        gif_url = get_gif("wave")
        if gif_url:
            await interaction.response.send_message(
                f"{interaction.user.mention} машет {member.mention} 👋", 
                embed=discord.Embed().set_image(url=gif_url)
            )
        else:
            await interaction.response.send_message("Не удалось получить гифку.")

    # Команда для подмигивания
    @app_commands.command(name="wink", description="Подмигнуть пользователю")
    async def wink(self, interaction: discord.Interaction, member: discord.Member):
        gif_url = get_gif("wink")
        if gif_url:
            await interaction.response.send_message(
                f"{interaction.user.mention} подмигивает {member.mention} 😉", 
                embed=discord.Embed().set_image(url=gif_url)
            )
        else:
            await interaction.response.send_message("Не удалось получить гифку.")

# Функция для подключения кода как расширения
async def setup(bot):
    await bot.add_cog(InteractionCommands(bot))
