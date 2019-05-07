import discord
from discord.ext import commands
import asyncio
import json
import os
#
prefix = ("$", ".")
bot = commands.Bot(command_prefix = prefix)

@bot.event
async def on_ready():

    print("-------------")
    print(bot.user.name)
    print(bot.user.id)
    print("-------------")

    AutoSpace = bot.get_cog("AutoSpace")
    bot.loop.create_task(AutoSpace.newLaunch())

    await bot.change_presence(activity = discord.Game("with itself"))

    print("Bot ready.")


@bot.command(pass_context = True)
async def close(ctx):
    await ctx.send("ciao")
    await bot.logout()

if __name__ == '__main__':
    #loading cogs
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            name = file[:-3]
            try:
                bot.load_extension("cogs.{}".format(name))
                print("{} loaded".format(name))
            except Exception as error:
                print("{} cannot be loaded <{}>".format(name, error))


with open("credentials.json", "r") as read_file:
    credentials = json.load(read_file)

bot.run(credentials["TOKEN"])
