import discord
from discord.ext import commands
import requests
import asyncio
import json

with open("credentials.json", "r") as read_file:
    credentials = json.load(read_file)


class AutoSpace(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def newLaunch(self):
        await self.bot.wait_until_ready()
        channel = self.bot.get_channel(481106726645399565)
        previousLaunchName = None

        while not self.bot.is_closed():
            response = requests.get("https://launchlibrary.net/1.4/launch/next/1")
            data = response.json()
            currentLaunchName = data["launches"][0]["name"]

            # checks if previous launch is the same as the current launch
            if (not (previousLaunchName == currentLaunchName)) or (previousLaunchName is None):
                await channel.send("Current launch is " + currentLaunchName)
                previousLaunchName = currentLaunchName
            else:
                await channel.send("No new launch")

            await asyncio.sleep(86400)  # every 24 hours

    async def apod(self):
        await self.bot.wait_until_ready()
        channel = self.bot.get_channel(481106726645399565)
        while not self.bot.is_closed():
            response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={credentials['NASA_API_KEY']}")
            data = response.json()
            results = f'''
            **{data["title"]}** - {data["date"]}

            {data["explanation"]}

            {data["url"]}'''

            await channel.send(results)
            await asyncio.sleep(86400)        

def setup(bot):
    bot.add_cog(AutoSpace(bot))
