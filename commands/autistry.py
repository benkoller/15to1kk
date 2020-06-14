import logging

from discord.ext import commands


class Autistry(commands.Cog):
    def __init__(self, bot, client=None):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx, *args, **kwargs):
        """Says hello"""
        member = ctx.author
        logging.debug(args, kwargs)
        await ctx.send('Hello {0.name}~, my fellow autist.'.format(member))

def setup(bot):
    bot.add_cog(Autistry(bot))