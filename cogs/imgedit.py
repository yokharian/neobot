#!/usr/bin/ python3
# -*- coding: <utf8> -*-
from discord.ext import commands


class ImgEdit(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.guild_only()
    @commands.command()
    async def getrandomuser(self, ctx):
        print("getting all users -->")


def setup(bot):
    bot.add_cog(ImgEdit(bot))
