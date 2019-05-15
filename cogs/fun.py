import discord
from discord.ext import commands
import random


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        # await ctx.send(f"{member.display_name}")
        await ctx.send("no")

    @commands.command(pass_context=True, name='8ball')
    async def ball(self, ctx):
        responses = ["As I see it, yes",
                     "Ask again later",
                     "Better not tell you now",
                     "Don't count on it",
                     "It is certain",
                     "Most likely",
                     "Outlook good",
                     "Outlook not so good",
                     "Without a doubt",
                     "Doubtful"]

        await ctx.send(random.choice(responses) + ", " + ctx.message.author.mention)


def setup(bot):
    bot.add_cog(Fun(bot))
