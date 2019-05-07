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
    bot.loop.create_task(test())
    await bot.change_presence(activity = discord.Game("with itself"))

    print("Bot ready")

async def test():
    await bot.wait_until_ready()
    while not bot.is_closed():
        channel = bot.get_channel(481106726645399565)
        await channel.send("background task")
        await asyncio.sleep(7)

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
