#!/usr/bin/ python3
# -*- coding: <utf8> -*-
from discord.ext import commands
import discord
import re


class ReaccionesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if(message.author.id == self.bot.mee6):
            pattern = re.compile("""^(GG ).+( [0-9]!)$""")
            levelUnderTen = re.match(pattern, message.content)
            if levelUnderTen:
                kpequeno = discord.utils.get(
                    self.bot.guild.emojis, name="kpequeno")
                await message.add_reaction(kpequeno)
            # todo handle ([1-9]) *10 levels


def setup(bot):
    bot.add_cog(ReaccionesCog(bot))
