#!/usr/bin/ python3
# -*- coding: <utf8> -*-
from decouple import config
import discord
from discord.ext.commands import Bot
startup_extensions = ["core.neobot"]
startup_extensions.extend(["cogs.imgedit", "cogs.reacciones"])


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class NeoBot(Bot, metaclass=Singleton):
    todoslosemojis: dict
    guild: discord.Guild

    def __init__(self, guildEnv: str, prefix: str) -> None:
        permitidoMencionar = discord.mentions.AllowedMentions(
            everyone=False, users=False, roles=False)
        super().__init__(command_prefix=prefix, fetch_offline_members=False, status=discord.Status.do_not_disturb,
                         allowed_mentions=permitidoMencionar, description="neo army x absolute customized discord bot ")
        self.guildEnv = guildEnv
        # hardcoded
        self.mee6 = 159985870458322944


if __name__ == "__main__":
    bot = NeoBot(config("GUILD"), config("PREFIX"))

    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.remove_command('help')

    bot.run(config("TOKEN"))
