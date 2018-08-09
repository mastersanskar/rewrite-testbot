import discord
from discord.ext import commands
import datetime

class Events:
    """Cog for events"""

    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        print(f'{datetime.datetime.now()}: Message from {message.author} in Guild: {message.guild} in Channel: {message.channel} ==> {message.content}')







def setup(bot):
    bot.add_cog(Events(bot))
