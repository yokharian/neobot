import discord
from discord.ext import commands
from decouple import config

bot = commands.Bot(command_prefix=config("PREFIX"))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(config("TOKEN"))
