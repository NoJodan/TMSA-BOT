import discord
from discord.ext import commands

EMBED_COLOR = 0x00ff00  # Color predeterminado para los embeds

class Stats(commands.Cog, name='stats'):
    def __init__(self, bot):
        self.bot = bot
        self.dbUsers = self.bot.mongo_manager["users"]

    @commands.hybrid_command(name='profile', aliases=['p'], description='View your profile or another user\'s profile.')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def profile(self, ctx, member: discord.Member=None):
        member = member or ctx.author

        try:
            user_data = self.dbUsers.find_one({"id": int(member.id)})
            if not user_data:
                await ctx.send(f"{member.mention} does not have an account registered.")
                return

            level = user_data.get('level', 'N/A')
            money = user_data.get('money', 'N/A')
            life = user_data.get('life', 'N/A')

            embed = discord.Embed(title=f"Profile of {member.name}",color=EMBED_COLOR)
            embed.add_field(name="Level", value=level, inline=True)
            embed.add_field(name="Money", value=money, inline=True)
            embed.add_field(name="Life", value=life, inline=True)
            embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)

            await ctx.send(embed=embed, ephemeral=True)
        except Exception as e:
            await ctx.send(f"An error occurred while retrieving the profile: {e}")

async def setup(bot):
    await bot.add_cog(Stats(bot))