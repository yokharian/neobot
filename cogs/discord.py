import discord

from io import BytesIO
from utils import default, permissions
from discord.ext import commands


class Discord_Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    @commands.command()
    @commands.guild_only()
    @commands.check(permissions.is_owner)
    async def avatar(self, ctx, *, user: discord.Member = None):
        """ Get the avatar of you or someone else """
        user = user or ctx.author
        avatar = user.avatar_url_as(size=1024)
        await ctx.send(f"Avatar of **{user.name}**\n{ avatar }")

    @commands.command()
    @commands.guild_only()
    @commands.check(permissions.is_owner)
    async def roles(self, ctx):
        """ Get all roles in current server """
        allroles = ""

        for num, role in enumerate(sorted(ctx.guild.roles, reverse=True), start=1):
            allroles += f"[{str(num).zfill(2)}] {role.id}\t{role.name}\t[ Users: {len(role.members)} ]\r\n"

        data = BytesIO(allroles.encode('utf-8'))
        await ctx.send(content=f"Roles in **{ctx.guild.name}**", file=discord.File(data, filename=f"{default.timetext('Roles')}"))

    @commands.group()
    @commands.guild_only()
    @commands.check(permissions.is_owner)
    async def server(self, ctx):
        """ Check info about current server """
        if ctx.invoked_subcommand is None:
            findbots = sum(1 for member in ctx.guild.members if member.bot)

            embed = discord.Embed()

            if ctx.guild.icon:
                embed.set_thumbnail(url=ctx.guild.icon_url)
            if ctx.guild.banner:
                embed.set_image(url=ctx.guild.banner_url_as(format="png"))

            embed.add_field(name="Server Name", value=ctx.guild.name, inline=True)
            embed.add_field(name="Server ID", value=ctx.guild.id, inline=True)
            embed.add_field(name="Members", value=ctx.guild.member_count, inline=True)
            embed.add_field(name="Bots", value=findbots, inline=True)
            embed.add_field(name="Owner", value=ctx.guild.owner, inline=True)
            embed.add_field(name="Region", value=ctx.guild.region, inline=True)
            embed.add_field(name="Created", value=default.date(ctx.guild.created_at), inline=True)
            await ctx.send(content=f"ℹ information about **{ctx.guild.name}**", embed=embed)

    @server.command(name="avatar", aliases=["icon"])
    @commands.check(permissions.is_owner)
    async def server_avatar(self, ctx):
        """ Get the current server icon """
        if not ctx.guild.icon:
            return await ctx.send("This server does not have a avatar...")
        await ctx.send(f"Avatar of **{ctx.guild.name}**\n{ctx.guild.icon_url_as(size=1024)}")

    @server.command(name="banner")
    @commands.check(permissions.is_owner)
    async def server_banner(self, ctx):
        """ Get the current banner image """
        if not ctx.guild.banner:
            return await ctx.send("This server does not have a banner...")
        await ctx.send(f"Banner of **{ctx.guild.name}**\n{ctx.guild.banner_url_as(format='png')}")


def setup(bot):
    bot.add_cog(Discord_Info(bot))
