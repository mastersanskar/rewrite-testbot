import discord
from discord.ext import commands

class Owner:
    """Commands for owner only"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='logout', aliases=['kill', 'die'])
    @commands.is_owner()
    async def do_logout(self, ctx):
        """Logs out the bot."""
        await ctx.send(f'RIP {self.bot.user}')
        await self.bot.logout()

    @commands.command(name='load')
    @commands.is_owner()
    async def cog_load(self, ctx, *, cog: str):
        """Command which Loads a Module."""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** [{e}]')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='unload')
    @commands.is_owner()
    async def cog_unload(self, ctx, *, cog: str):
        """Command which Unloads a Module."""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** [{e}]')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='reload')
    @commands.is_owner()
    async def cog_reload(self, ctx, *, cog: str):
        """Command which Reloads a Module."""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** [{e}]')
        else:
            await ctx.send('**`SUCCESS`**')


def setup(bot):
    bot.add_cog(Owner(bot))
