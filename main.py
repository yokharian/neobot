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
        for guild in bot.guilds:
            # i know not secure
            if "NeoArmy" == config("GUILD"):
                bot.guild = guild

        print(f'{bot.user} is connected to {bot.guild.name}(id: {bot.guild.id})')
        # <Emoji id=681228742713933946 name='kpequeno' animated=False managed=False>
        todoslosemojis.append(discord.utils.get(
            bot.guild.emojis, name='kpequeno'))

    @bot.listen()
    async def on_message(message):
        print(message.content)
        if(message.author.id == 159985870458322944):
            # pattern can be optimized
            print("mee6")
            pattern = re.compile("""^(GG <@!)[0-9]+>([A-Za-z ,]+)([0-9]!)$""")
            levelUnderTen = re.match(pattern, message.content)
            print(message.content)
            if levelUnderTen:
                print("omg")
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
