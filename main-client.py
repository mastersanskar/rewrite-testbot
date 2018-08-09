import the_token

import discord
from discord.ext import commands

initial_extensions = ['cogs.basic_cmds', 'cogs.owner', 'cogs.events']

bot = commands.Bot(command_prefix=commands.when_mentioned_or('//'))

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'{extension} cannot be loaded. [{e}]')

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')
    print (discord.__version__)
    await bot.change_presence(activity=discord.Game('testing the bot'))

    #await bot.process_commands(message)

bot.run(the_token.mytoken)
