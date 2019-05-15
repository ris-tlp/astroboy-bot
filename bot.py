import discord
from discord.ext import commands
import asyncio
import json
import os

prefix = ("$", ".")
bot = commands.Bot(command_prefix=prefix)


@bot.event
async def on_ready():
    print("-------------")
    print("User::" + bot.user.name)
    print("ID::" + str(bot.user.id))
    print("Version::" + discord.__version__)
    print("-------------")

    AutoSpace = bot.get_cog("AutoSpace")
    bot.loop.create_task(AutoSpace.newLaunch())
    bot.loop.create_task(AutoSpace.apod())

    await bot.change_presence(activity=discord.Game("with itself"))
    print("Bot ready.")


@bot.command(pass_context=True)
async def close(ctx):
    await ctx.send("ciao")
    await bot.logout()


@bot.command(pass_context=True)
async def load(ctx, extension):
    try:
        bot.load_extension("cogs.{}".format(extension))
        print("{} manually loaded".format(extension))
        await ctx.send("\"{}\"cog manually loaded".format(extension))
    except Exception as error:
        print("{} could not be loaded. <{}>".format(extension, error))


@bot.command(pass_context=True)
async def unload(ctx, extension):
    try:
        bot.unload_extension("cogs.{}".format(extension))
        print("{} manually unloaded".format(extension))
        await ctx.send("\"{}\"cog manually unloaded".format(extension))
    except Exception as error:
        print("{} could not be unloaded. <{}>".format(extension, error))


@bot.command(pass_context=True)
async def reset(ctx, extension):
    try:
        bot.unload_extension("cogs.{}".format(extension))
        bot.load_extension("cogs.{}".format(extension))
        await ctx.send(f"{extension} cog reset")
    except Exception as error:
        await ctx.send(error)


@bot.command(pass_context=True)
async def github(ctx):
    '''Returns the github repo of this bot'''
    await ctx.send("https://github.com/ris-tlp/astroboy-bot")


if __name__ == '__main__':
    # loading cogs
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
