import discord
from discord.ext import commands
import json
import os

prefix = ("$", ".")
bot = commands.Bot(command_prefix = prefix)

extensions = ['cogs.fun', 'cogs.manualSpace']

@bot.event
async def on_ready():
    await bot.change_presence(game = discord.Game(name = "with itself"))
    print("Bot running.")

@bot.command(pass_context = True)
async def close(ctx):
    await bot.say("ciao")
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
