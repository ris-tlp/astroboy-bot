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

            result = (
                f'**{data["title"]}** - {data["date"]}\n'
                f'{data["explanation"]}\n'
                f'{data["url"]}'
            )

            await ctx.send(result)
        except Exception as e:
            await ctx.send(f'Encountered an error: {e}')

    @commands.command(pass_context=True)
    async def rocket(self, ctx):
        """Gets information about a rocket through its name"""

        rocketName = ctx.message.content[8:]
        try:
            response = requests.get(
                f"https://launchlibrary.net/1.4/rocket/{rocketName}")
            data = response.json()

            if(data["total"] != 0):
                result = f'Here\'s what I found {ctx.message.author.mention}:\n\n'

                for rocket in data["rockets"]:
                    result += f'ID: {rocket["id"]} | Name: {rocket["name"]}\n'

                result += '\nYou can find more information through .rocketid using the rocket\'s ID.'
                await ctx.send(result)
            else:
                await ctx.send("No results.")
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

                result = (
                    f'**ID**: {str(rocket["id"])}\n'
                    f'**Name**: {rocket["name"]}\n'
                    "**Agencies**: "
                )
                
                for agency in dataForFamily["RocketFamilies"][0]["agencies"]:
                    result += f'{agency["name"]}, '

                result += (
                    '\n'
                    f'**More information at**: {rocket["infoURLs"]}\n'
                    f'{rocket["imageURL"]}'
                )

                await ctx.send(result)
            else:
                await ctx.send("No results.")
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
            result = (
                f'**Name**: {launch["name"]}\n'
                f'**Launch window**: {launch["windowstart"]}\n'
                f'**Location**: {launch["location"]["pads"][0]["name"]}\n'
                f'**Webcast**: {launch["vidURLs"]}'
            )

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
                agency = data["agencies"][0]
                result = (
                    f'**ID**: {agency["id"]}\n'
                    f'**Name**: {agency["name"]}\n'
                    f'**Country code**: {agency["countryCode"]}\n'
                    f'**Website**: {agency["infoURL"]}\n'
                    f'**Wikipedia**: {agency["wikiURL"]}\n'
                )
                await ctx.send(result)
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

            if (data["total"] != 0):
                result = f'Here\'s what I found {ctx.message.author.mention}\n'

                for agency in data["agencies"]:
                    result += f'{str(agency["id"])}. {agency["name"]} - {agency["abbrev"]}\n'
                        
                result += "You can find more information by searching the abbreviation using .abbrev or by ID using .agencyid."
                await ctx.send(result)
            else:
                await ctx.send("No results.")
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
                agency = data["agencies"][0]
                result = (
                    f'**Name**: {agency["name"]}\n'
                    f'**Country code**: {agency["countryCode"]}\n'
                    f'**Website**: {agency["infoURL"]}\n'
                    f'**Wikipedia**: {agency["wikiURL"]}\n'
                )
                await ctx.send(result)
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
                result = f'Here\'s what I found {ctx.message.author.mention}:\n\n'

                for mission in data["missions"]:
                    result += f'{mission["id"]}. {mission["name"]}\n'
                result += "You can find more information by searching through ID using .missionid"
                    
                await ctx.send(result)

            else:
                await ctx.send("No results.")
        except Exception as e:
            await ctx.send(f"Encountered an error: {e}")

    @commands.command(pass_context=True)
    async def missionid(self, ctx):
        """Gets information about missions by ID"""

        missionID = str(ctx.message.content[11:])
        try:
            response = requests.get(
                f"https://launchlibrary.net/1.4/mission/{missionID}")
            data = response.json()

            if(data["total"] != 0):
                mission = data["missions"][0]
                result = f'{mission["id"]}. **{mission["name"]}** - {mission["description"]}'
                await ctx.send(result)
            else:
                await ctx.send("No results.")
        except Exception as e:
            await ctx.send(f"Encountered an error: {e}")


def setup(bot):
    bot.add_cog(ManualSpace(bot))
