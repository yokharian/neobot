# from random import randint
import re
import discord
from discord.ext import commands
from decouple import config

if __name__ == "__main__":
    # Mala práctica, TODO add object wrapper of the commands.Bot
    todoslosemojis = []
    permitidoMencionar = discord.mentions.AllowedMentions(
        everyone=False, users=False, roles=False)
    bot = commands.Bot(command_prefix=config("PREFIX"), fetch_offline_members=False, status=discord.Status.do_not_disturb,
                       allowed_mentions=permitidoMencionar)

    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')

    @bot.event
    async def on_ready():
        bot.MEE6ID = 159985870458322944
        for guild in bot.guilds:
            if guild.name == config("GUILD"):
                bot.guild = guild

        print(f'{bot.user} is connected to {bot.guild.name}(id: {bot.guild.id})')
        todoslosemojis.append(discord.utils.get(
            bot.guild.emojis, name='kpequeno'))

    @bot.listen()
    async def on_message(message):
        if(message.author.id == bot.MEE6ID):
            # pattern can be optimized
            pattern = re.compile("""^(GG <@!)[0-9]+>,([a-z ]+)[0-9]!$""")
            levelUnderTen = re.match(pattern, message.content)

            if levelUnderTen:
                await message.add_reaction(todoslosemojis[0])

        # Handled at the end cuz, this bot will rarely speak
        if message.author == bot.user:
            return

    @bot.event
    async def on_error(event, *args, **kwargs):
        print("--- ERROR ---")
        print("event:\n", event)
        print("args:\n", args)
        print("kwargs:\n", kwargs)

    bot.run(config("TOKEN"))
