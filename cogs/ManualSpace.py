import discord
from discord.ext import commands
import requests
import json


with open("credentials.json", "r") as read_file:
    credentials = json.load(read_file)


class ManualSpace(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def pos(self, ctx):
        """Returns the number and names of people currently in space"""

        try:
            response = requests.get("http://api.open-notify.org/astros.json")
            data = response.json()
            result = f'Number: {data["number"]}\n'

            for astronaut in data["people"]:
                result += f'Craft: {astronaut["craft"]} | '
                result += f'Name: {astronaut["name"]} \n'

            await ctx.send(result)
            
        except Exception as e:
            await ctx.send("Encountered an error: {e}")

    @commands.command(pass_context=True)
    async def apod(self, ctx):
        """Manually fetches the Astronomy Picture of the Day"""

        try:
            response = requests.get(
                f'https://api.nasa.gov/planetary/apod?api_key={credentials["NASA_API_KEY"]}')
            data = response.json()
            results = f'''
            **{data["title"]}** - {data["date"]}\n
            {data["explanation"]}\n
            {data["url"]}'''

            await ctx.send(results)
        except Error as e:
            await ctx.send(f"Encountered an error: {e}")

    @commands.command(pass_context=True)
    async def rocket(self, ctx):
        """Gets information about a rocket through its name"""

        rocketName = ctx.message.content[8:]
        try:
            response = requests.get(
                f"https://launchlibrary.net/1.4/rocket/{rocketName}")
            data = response.json()

            if(data["total"] != 0):
                result = "Here's what I found " + ctx.message.author.mention + "\n\n"
                initialLength = len(result)

                for rocket in data["rockets"]:
                    result += f'ID: {rocket["id"]} | Name: {rocket["name"]}\n'

                result += "\nYou can find more information through .rocketid using the rocket's ID."
            else:
                result = "No results."

            await ctx.send(result)
        except Exception as e:
            await ctx.send("Encountered an error: {e}")

    @commands.command(pass_context=True)
    async def rocketid(self, ctx):
        """Gets information about a rocket through its ID"""

        rocketID = str(ctx.message.content[10:])
        try:
            response = requests.get(
                f"https://launchlibrary.net/1.4/rocket/{rocketID}")
            data = response.json()

            if(data["total"] != 0):
                responseForFamily = requests.get(
                    f'https://launchlibrary.net/1.4/rocketfamily/{data["rockets"][0]["family"]["id"]}')
                dataForFamily = responseForFamily.json()
                rocket = data["rockets"][0]

                result = ""
                result += "**ID**: " + str(rocket["id"]) + "\n"
                result += "**Name**: " + rocket["name"] + "\n"
                result += "**Agencies**: "

                for agency in dataForFamily["RocketFamilies"][0]["agencies"]:
                    result += agency["name"] + ", "

                result += "\n"
                result += "**More information at**: " + \
                    rocket["infoURLs"][0] + "\n"
                result += rocket["imageURL"]
            else:
                result = "No results."

            await ctx.send(result)
        except Exception as e:
            await ctx.send("Encountered an error: {e}")

    @commands.command(pass_context=True)
    async def nextlaunch(self, ctx):
        """Gets information about the next upcoming launch"""
        try:
            response = requests.get(
                "https://launchlibrary.net/1.4/launch/next/1")
            data = response.json()
            launch = data["launches"][0]
            result = f'**Name**: {launch["name"]} \n **Launch window**: {launch["windowstart"]} \n **Location**: {launch["location"]["pads"][0]["name"]} \n **Webcast**: {launch["vidURLs"]}'

            await ctx.send(result)
        except Exception as e:
            await ctx.send("Encountered an error: {e}")

    @commands.command(pass_context=True)
    async def abbrev(self, ctx):
        """Gets info about an agency through it's abbreviation (NASA)"""

        abbr = ctx.message.content[8:]
        try:
            response = requests.get(
                f'https://launchlibrary.net/1.4/agency/{abbr}')
            data = response.json()

            if(data["total"] != 0):
                await ctx.send("ID: " + str(data["agencies"][0]["id"]) + "\n" +
                            "Name: " + data["agencies"][0]["name"] + "\n" +
                            "Country code: " +
                            data["agencies"][0]["countryCode"] + "\n"
                            + "Website: " + data["agencies"][0]["infoURL"] + "\n" +
                            "Wikipedia: " + data["agencies"][0]["wikiURL"])
            else:
                await ctx.send("No results.")
        except Exception as e:
            await ctx.send(f"Encountered an error: {e}")

    @commands.command(pass_context=True)
    async def agency(self, ctx):
        """Gets info about an agency through it's name"""
        name = ctx.message.content[8:]
        name.replace(" ", "&")
        try:
            response = requests.get(
                f'https://launchlibrary.net/1.4/agency?name={name}')
            data = response.json()
            results = "Here's what I found: " + ctx.message.author.mention + "\n"
            initialLength = len(results)

            for agency in data["agencies"]:
                results += "{}. {} - {}\n".format(
                    str(agency["id"]), agency["name"], agency["abbrev"])

            if len(results) > initialLength:
                results = results + "\n" + \
                    "You can find more information by searching the abbreviation using .abbrev or by ID using .agencyid"
            else:
                results = "No results."

            await ctx.send(results)
        except Exception as e:
            await ctx.send("Encountered an error: {e}")

    @commands.command(pass_context=True)
    async def agencyid(self, ctx):
        """Gets information about agency using it's ID"""

        idInput = ctx.message.content[10:]

        try:
            response = requests.get(
                f'https://launchlibrary.net/1.4/agency/{idInput}')
            data = response.json()

            if(data["total"] != 0):
                await ctx.send("Name: " + data["agencies"][0]["name"] + "\n" +
                            "Country code: " +
                            data["agencies"][0]["countryCode"] + "\n"
                            + "Website: " + data["agencies"][0]["infoURL"] + "\n" +
                            "Wikipedia: " + data["agencies"][0]["wikiURL"])
            else:
                await ctx.send("No results.")

        except Exception as e:
            await ctx.send(f"Encountered an error: {e}")

    @commands.command(pass_context=True)
    async def mission(self, ctx):
        """Gets information about missions by name"""

        missionName = ctx.message.content[9:]
        missionName.replace(" ", "&")
        try:
            response = requests.get(
                f'https://launchlibrary.net/1.4/mission/{missionName}')
            data = response.json()
            if(data["total"] != 0):
                    
                results = "Here's what I found: " + ctx.message.author.mention + "\n\n"
                initialLength = len(results)

                for mission in data["missions"]:
                    results += "{}. {}\n".format(mission["id"], mission["name"])
                
                results = results + "\n" + \
                    "You can find more information by searching through ID using .missionid"

            else:
                results = "No results."

            await ctx.send(results)

        except Exception as e:
            await ctx.send("Encountered an error: {e}")

    @commands.command(pass_context=True)
    async def missionid(self, ctx):
        """Gets information about missions by ID"""

        missionID = str(ctx.message.content[11:])
        try:
            response = requests.get(
                f"https://launchlibrary.net/1.4/mission/{missionID}")
            data = response.json()

            if(data["total"] != 0):
                await ctx.send("{}. **{}** - {}"
                            .format(data["missions"][0]["id"], data["missions"][0]["name"],
                                    data["missions"][0]["description"]))
            else:
                await ctx.send("No results.")
        except Exception as e:
            await ctx.send(f"Encountered an error: {e}")


def setup(bot):
    bot.add_cog(ManualSpace(bot))
