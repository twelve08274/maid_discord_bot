import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f"{bot.user} が起動しました！")


@bot.command()
async def ping(ctx):
    await ctx.send("pong!")


bot.run(TOKEN)
