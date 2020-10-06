from discord.ext import commands
from utils import permissions


class ImgEdit(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.check(permissions.is_owner)
    async def getrandomuser(self, ctx):
        print("getting all users -->")


def setup(bot):
    bot.add_cog(ImgEdit(bot))
