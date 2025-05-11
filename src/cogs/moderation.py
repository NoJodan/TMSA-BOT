from discord.ext import commands

# IDs de administradores permitidos
ADMIN_IDS = [452498453394751538]

class ModerationCog(commands.Cog, name='Moderation'):
    def __init__(self, bot):
        self.bot = bot
        self.dbUsers = self.bot.mongo_manager["users"]

    async def _is_admin(self, user_id):
        return user_id in ADMIN_IDS

    async def _send_error(self, ctx, message):
        await ctx.send(f"{ctx.author.mention} {message}", ephemeral=True)

    @commands.hybrid_command(name='reloadcog', aliases=['rcog'], description='Reload a cog')
    async def reload_cog(self, ctx, cog_name: str = None):
        if not await self._is_admin(ctx.message.author.id):
            await self._send_error(ctx, "You do not have permission to use this command.")
            return

        if not cog_name:
            await self._send_error(ctx, "Please provide a cog name to reload, use `reloadcog <cog_name>`.")
            return

        try:
            await self.bot.reload_extension(f'cogs.{cog_name}')
            await ctx.send(f"{ctx.author.mention} Reloaded cog: {cog_name}", ephemeral=True)
        except Exception as e:
            await self._send_error(ctx, f"Error reloading cog: {e}")

    @commands.hybrid_command(name='unloadcog', aliases=['ucog'], description='Unload a cog')
    async def unload_cog(self, ctx, cog_name: str = None):
        if not await self._is_admin(ctx.message.author.id):
            await self._send_error(ctx, "You do not have permission to use this command.")
            return

        if not cog_name:
            await self._send_error(ctx, "Please provide a cog name to unload, use `unloadcog <cog_name>`.")
            return

        try:
            await self.bot.unload_extension(f'cogs.{cog_name}')
            await ctx.send(f"{ctx.author.mention} Unloaded cog: {cog_name}", ephemeral=True)
        except Exception as e:
            await self._send_error(ctx, f"Error unloading cog: {e}")

    @commands.hybrid_command(name='loadcog', aliases=['lcog'], description='Load a cog')
    async def load_cog(self, ctx, cog_name: str = None):
        if not await self._is_admin(ctx.message.author.id):
            await self._send_error(ctx, "You do not have permission to use this command.")
            return

        if not cog_name:
            await self._send_error(ctx, "Please provide a cog name to load, use `loadcog <cog_name>`.")
            return

        try:
            await self.bot.load_extension(f'cogs.{cog_name}')
            await ctx.send(f"{ctx.author.mention} Loaded cog: {cog_name}", ephemeral=True)
        except Exception as e:
            await self._send_error(ctx, f"Error loading cog: {e}")

    @commands.hybrid_command(name='showusers', aliases=['users'], description='Show all users in the database')
    async def show_users(self, ctx):
        try:
            documents = self.dbUsers.find()
            users = [str(doc) for doc in documents]

            if not users:
                await ctx.send("No hay usuarios en la colección.", ephemeral=True)
                return

            message = "\n".join(users)
            if len(message) > 2000:  # Discord tiene un límite de 2000 caracteres por mensaje
                await ctx.send("La lista de usuarios es demasiado larga para enviarla en un solo mensaje.", ephemeral=True)
            else:
                await ctx.send(f"Usuarios en la colección:\n{message}", ephemeral=True)
        except Exception as e:
            await self._send_error(ctx, f"Error al acceder a la base de datos: {e}")

async def setup(bot):
    await bot.add_cog(ModerationCog(bot))
