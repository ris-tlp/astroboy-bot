import discord
from discord.ext import commands
import requests

class manualSpace(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def nextlaunch(self, ctx):
        response = requests.get("https://launchlibrary.net/1.4/launch/next/1")
        data = response.json()
        await ctx.send("API status code: {}".format(response.status_code))
        await ctx.send("Name of launch <**{}".format(data["launches"][0]["name"]
         + "**> has a launch window from <**" + data["launches"][0]["windowstart"]
          + "**> at <**" + data["launches"][0]["location"]["pads"][0]["name"] +
          "**> and will be streamed on " + data["launches"][0]["vidURLs"][0]))

def setup(bot):
    bot.add_cog(manualSpace(bot))
