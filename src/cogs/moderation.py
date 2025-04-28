from discord.ext import commands

config = ["lawliet0_0"]

class ModerationCog(commands.Cog, name='Moderation'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='reloadcog', aliases=['rcog'])
    async def reload_cog(self, ctx, cog_name: str):
        if ctx.message.author.id in config["moderators"]:
            if not cog_name:
                await ctx.send(f"{ctx.author.mention} Please provide a cog name to reload, use `reloadcog <cog_name>`")
            else:
                try:
                    await self.bot.reload_extension(f'cogs.{cog_name}')
                    await ctx.send(f"{ctx.author.mention} Reloaded cog: {cog_name}")
                except Exception as e:
                    await ctx.send(f"{ctx.author.mention} Error reloading cog: {e}")
        else:
            await ctx.send(f"{ctx.author.mention} You do not have permission to use this command.")
    
    @commands.command(name='unloadcog', aliases=['ucog'])
    async def unload_cog(self, ctx, cog_name: str):
        if ctx.message.author.id in config["moderators"]:
            if not cog_name:
                await ctx.send(f"{ctx.author.mention} Please provide a cog name to unload, use `unloadcog <cog_name>`")
            else:
                try:
                    await self.bot.unload_extension(f'cogs.{cog_name}')
                    await ctx.send(f"{ctx.author.mention} Unloaded cog: {cog_name}")
                except Exception as e:
                    await ctx.send(f"{ctx.author.mention} Error unloading cog: {e}")
        else:
            await ctx.send(f"{ctx.author.mention} You do not have permission to use this command.")
    
    @commands.command(name='loadcog', aliases=['lcog'])
    async def load_cog(self, ctx, cog_name: str):
        if ctx.message.author.id in config["moderators"]:
            if not cog_name:
                await ctx.send(f"{ctx.author.mention} Please provide a cog name to load, use `loadcog <cog_name>`")
            else:
                try:
                    await self.bot.load_extension(f'cogs.{cog_name}')
                    await ctx.send(f"{ctx.author.mention} Loaded cog: {cog_name}")
                except Exception as e:
                    await ctx.send(f"{ctx.author.mention} Error loading cog: {e}")
        else:
            await ctx.send(f"{ctx.author.mention} You do not have permission to use this command.")

async def setup(bot):
    await bot.add_cog(ModerationCog(bot))