import discord
from discord.ext import commands

class ExampleCog(commands.Cog, name='Example'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='example', aliases=['ex'])
    async def example(self, ctx):
        print("example command executed")
        await ctx.send('This is an example command!')

async def setup(bot):
    await bot.add_cog(ExampleCog(bot))