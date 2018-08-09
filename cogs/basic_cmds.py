import discord
from discord.ext import commands

class Basic:
    """Basic commands for all users"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='say', aliases=['echo', 'repeat', 'mimic'])
    async def do_say(self, ctx, *, args: str):
        """It repeats what's said"""
        await ctx.send(args)

def setup(bot):
    bot.add_cog(Basic(bot))
