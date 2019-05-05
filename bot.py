import discord
import json
from discord.ext import commands

prefix = ("$")
bot = commands.Bot(command_prefix = prefix)

extensions = ['cogs.fun']

@bot.event
async def on_ready():
    await bot.change_presence(game = discord.Game(name = "with itself"))
    print("Bot running.")

@bot.command(pass_context = True)
async def close(ctx):
    await bot.say("ciao")
    await bot.logout()

if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
            print("{} loaded".format(extension))
        except Exception as error:
            print("{} cannot be loaded. [{}]".format(extension, error))


with open("credentials.json", "r") as read_file:
    credentials = json.load(read_file)

bot.run(credentials["TOKEN"])
