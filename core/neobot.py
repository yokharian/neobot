#!/usr/bin/ python3
# -*- coding: <utf8> -*-
from discord.ext import commands


class MyHelpCommand(commands.MinimalHelpCommand):
    def get_command_signature(self, command):
        return '{0.clean_prefix}{1.qualified_name} {1.signature}'.format(self, command)


class CoreCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._original_help_command = bot.help_command
        bot.help_command = MyHelpCommand()
        bot.help_command.cog = self

    def cog_unload(self):
        self.bot.help_command = self._original_help_command

    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            print(guild.name)
            if guild.name == self.bot.guildEnv:
                self.bot.guild = guild
        print(
            f'{self.bot.user} is connected to {self.bot.guild.name}(id: {self.bot.guild.id})')

    # TODO message broker
    @commands.Cog.listener()
    async def on_error(self, event, *args, **kwargs):
        print("--- ERROR ---")
        print("event:\n", event)
        print("args:\n", args)
        print("kwargs:\n", kwargs)


def setup(bot):
    bot.add_cog(CoreCog(bot))
