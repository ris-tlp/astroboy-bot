import discord
from discord.ext import commands
import requests

class ManualSpace(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def nextlaunch(self, ctx):
        """Gets information about the next upcoming launch"""

        response = requests.get("https://launchlibrary.net/1.4/launch/next/1")
        data = response.json()
        await ctx.send("API status code: {}".format(response.status_code))
        await ctx.send("Name of launch <**{}".format(data["launches"][0]["name"]
         + "**> has a launch window from <**" + data["launches"][0]["windowstart"]
          + "**> at <**" + data["launches"][0]["location"]["pads"][0]["name"] +
          "**> and will be streamed on " + data["launches"][0]["vidURLs"][0]))


    @commands.command(pass_context = True)
    async def abbrev(self, ctx):
        """Gets information about an abbreviated agency"""

        abbr = ctx.message.content[8:]
        response = requests.get("https://launchlibrary.net/1.4/agency/{}".format(abbr))
        data = response.json()

        await ctx.send("Name: " + data["agencies"][0]["name"] + "\n" +
                "Country code: " + data["agencies"][0]["countryCode"] + "\n"
                + "Website: " + data["agencies"][0]["infoURL"] + "\n" +
                "Wikipedia: " + data["agencies"][0]["wikiURL"])

    @commands.command(pass_context = True)
    async def agency(self, ctx):
        """Gets information about an agency"""

        name = ctx.message.content[8:]
        name.replace(" ", "&")
        response = requests.get("https://launchlibrary.net/1.4/agency?name={}".format(name))
        data = response.json()
        results = ""

        for agency in data["agencies"]:
            results += "{}. {} - {}\n".format(str(agency["id"]), agency["name"], agency["abbrev"])

        results = "Here's what I found: " + ctx.message.author.mention + "\n" + results
        results = results + "\n" + "You can find more information by searching the abbreviation using .abbrev or by ID using .agencyid"
        await ctx.send(results)

    @commands.command(pass_context = True)
    async def agencyid(self, ctx):
        """Gets information about agency using ID"""

        idinput = ctx.message.content[10:]
        response = requests.get("https://launchlibrary.net/1.4/agency/{}".format(idinput))
        data = response.json()

        await ctx.send("Name: " + data["agencies"][0]["name"] + "\n" +
                "Country code: " + data["agencies"][0]["countryCode"] + "\n"
                + "Website: " + data["agencies"][0]["infoURL"] + "\n" +
                "Wikipedia: " + data["agencies"][0]["wikiURL"])


def setup(bot):
    bot.add_cog(ManualSpace(bot))
