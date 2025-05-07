import discord
from discord.ext import commands

class Start(commands.Cog, name = 'start'):
    def __init__(self, bot):
        self.bot = bot
        self.dbUsers = self.bot.mongo_manager["users"]
        
    @commands.command(name = 'start')
    async def start(self, ctx):
        
        startinfo = '''```
Category: Main\n
Dificulty: F\n
Clear condition: Use the basic commands\n
Time limit: 1 hour\n
Compensation: 300 coins\n
Failure: Death```'''
        
        embed = discord.Embed(title = '[The free service of planetary system 8612 has been terminated.]\n[The main scenario has started.]',
                              description = 'You have been living too long for free. Isn\'t life too generous? You were born and paid no price for breathing, eating, pooping and breeding! Ha! You really live in a good world!',
                              color = 0xcf010b)
        embed.add_field(name = '[Main scenario #1-System test]', value = f'{startinfo}', inline = False)
        embed.add_field(name = '[Then, good luck everyone. Please show me an interesting story.]', value = ':white_small_square: For more information use `help` and `help <command>` for a detailed explanation.')
        embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/838781843763494952/1366595658261205133/Bihyung_29.webp?ex=681184e3&is=68103363&hm=8c1fab2cc114e4f2fcae12d8475292ceb8ee037ace565eb9ba9400c83b775ad1&')

        payload = {'id'         :       int(ctx.message.author.id),
                   'name'       :       ctx.message.author.name,
                   'level'      :       1,
                   'sponsor'    :       'None',
                   'atk'        :       1,
                   'def'        :       1,
                   'agi'        :       1,
                   'mag'        :       1,
                   'life'       :       10,
                   'money'      :       10,
                   'weapon'     :       0,
                   'armor'      :       0,
                   'inv'        :       {'knife' :  1},
                   'skills'     :       {'Reader':  1},
                   'stigmata'   :       ['None'],
                   'stories'    :       ['None'],
                   'quests'     :       ['None'],
                   'isConstellation' :   0,
                   'nebula'     :       'None',
                   'oncommand'  :       0,
                   'dateCreate' :       ctx.message.created_at}
        
        users_list = []
        for user in self.dbUsers.find():
            users_list.append(int(user['id']))
        
        if int(ctx.message.author.id) in users_list:
            await ctx.send(f"{ctx.message.author.mention} You already have the account registered.")
        else:
            self.dbUsers.insert_one(payload)
            await ctx.send(f"{ctx.message.author.mention} Successfully registered account.")
            await ctx.send(embed = embed)
        
async def setup(bot):
    await bot.add_cog(Start(bot))