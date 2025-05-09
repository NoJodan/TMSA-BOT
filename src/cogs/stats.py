import discord
from discord.ext import commands

class Stats(commands.Cog, name = 'stats'):
    def __init__(self, bot):
        self.bot = bot
        self.dbUsers = self.bot.mongo_manager["users"]

    @commands.hybrid_command(name = 'profile', aliases = ['p'], description = 'View your profile or another user\'s profile.')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def profile(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        
        user_data = self.dbUsers.find_one({"id": int(member.id)})
        
        if user_data is None:
            await ctx.send(f"{member.mention} does not have an account registered.")
            return
        
        embed = discord.Embed(title=f"Profile of {member.name}", color=0x00ff00)
        embed.add_field(name="Level", value=user_data['level'], inline=True)
        embed.add_field(name="Money", value=user_data['money'], inline=True)
        embed.add_field(name="Life", value=user_data['life'], inline=True)
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)

        await ctx.send(embed=embed, ephemeral=True)
        
        
async def setup(bot):
    await bot.add_cog(Stats(bot))