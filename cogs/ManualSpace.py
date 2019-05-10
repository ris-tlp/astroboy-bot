import discord
from discord.ext import commands
import requests


class ManualSpace(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def nextlaunch(self, ctx):
        """Gets information about the next upcoming launch"""

        response = requests.get("https://launchlibrary.net/1.4/launch/next/1")
        data = response.json()
        await ctx.send("API status code: {}".format(response.status_code))
        await ctx.send("Name of launch <**{}".format(data["launches"][0]["name"]
                                                     + "**> has a launch window from <**" + data["launches"][0][
                                                         "windowstart"]
                                                     + "**> at <**" + data["launches"][0]["location"]["pads"][0][
                                                         "name"] +
                                                     "**> and will be streamed on " + data["launches"][0]["vidURLs"][
                                                         0]))

    @commands.command(pass_context=True)
    async def abbrev(self, ctx):
        """Gets info about an agency through it's abbreviation (NASA)"""

        abbr = ctx.message.content[8:]
        response = requests.get("https://launchlibrary.net/1.4/agency/{}".format(abbr))
        data = response.json()

        await ctx.send("ID: " + str(data["agencies"][0]["id"]) + "\n" +
                       "Name: " + data["agencies"][0]["name"] + "\n" +
                       "Country code: " + data["agencies"][0]["countryCode"] + "\n"
                       + "Website: " + data["agencies"][0]["infoURL"] + "\n" +
                       "Wikipedia: " + data["agencies"][0]["wikiURL"])

    @commands.command(pass_context=True)
    async def agency(self, ctx):
        """Gets info about an agency through it's name"""

        name = ctx.message.content[8:]
        name.replace(" ", "&")
        response = requests.get("https://launchlibrary.net/1.4/agency?name={}".format(name))
        data = response.json()
        results = "Here's what I found: " + ctx.message.author.mention + "\n"
        initialLength = len(results)

        for agency in data["agencies"]:
            results += "{}. {} - {}\n".format(str(agency["id"]), agency["name"], agency["abbrev"])

        if len(results) > initialLength:
            results = results + "\n" + "You can find more information by searching the abbreviation using .abbrev or by ID using .agencyid"
        else:
            results = "No results."

        await ctx.send(results)

    @commands.command(pass_context=True)
    async def agencyid(self, ctx):
        """Gets information about agency using it's ID"""

        idInput = ctx.message.content[10:]
        response = requests.get("https://launchlibrary.net/1.4/agency/{}".format(idInput))
        data = response.json()

        await ctx.send("Name: " + data["agencies"][0]["name"] + "\n" +
                       "Country code: " + data["agencies"][0]["countryCode"] + "\n"
                       + "Website: " + data["agencies"][0]["infoURL"] + "\n" +
                       "Wikipedia: " + data["agencies"][0]["wikiURL"])

    @commands.command(pass_context=True)
    async def mission(self, ctx):
        """Gets information about missions by name"""

        missionName = ctx.message.content[9:]
        missionName.replace(" ", "&")
        response = requests.get("https://launchlibrary.net/1.4/mission/{}".format(missionName))
        data = response.json()
        results = "Here's what I found: " + ctx.message.author.mention + "\n\n"
        initialLength = len(results)

        for mission in data["missions"]:
            results += "{}. {}\n".format(mission["id"], mission["name"])

        if len(results) > initialLength:
            results = results + "\n" + "You can find more information by searching through ID using .missionid"
        else:
            results = "No results."

        await ctx.send(results)

    @commands.command(pass_context=True)
    async def missionid(self, ctx):
        """Gets information about missions by ID"""

        missionID = str(ctx.message.content[11:])
        response = requests.get("https://launchlibrary.net/1.4/mission/{}".format(missionID))
        data = response.json()

        await ctx.send("{}. **{}** - {}"
                       .format(data["missions"][0]["id"], data["missions"][0]["name"],
                               data["missions"][0]["description"]))


def setup(bot):
    bot.add_cog(ManualSpace(bot))
