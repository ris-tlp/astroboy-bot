Astroboy (in progress)
=========

A discord bot that notifies of upcoming launches by various space agencies every 24 hours with additional commands. This bot uses the [launchlibrary API](https://launchlibrary.net/docs/1.4/api.html)

Uses [discord.py](https://github.com/Rapptz/discord.py) version ```1.0.1``` so you need to use python `3.5` or higher.

## Instructions
1. `python -m pip install requirements.txt` to install necessary packages.  
2. Replace token with your bot's token in `credentials.json`.  
3. Run `bot.py`. That's all!  


## Commands

### Bot 
* `close`: Closes the bot and logs out all instances.
* `load <extension>`: Manually loads a cog through its name `<extension>`.
* `unload <extension>`: Manually unloads a cog through its name `<extensions>`.

### ManualSpace Cog
* `nextlaunch`: Makes a GET request and responds with the next upcoming launch's name, location, launch window and stream link.
* `agency <name>`: Makes a GET request and returns a list of all the matches' ID, full name and abbreviation.
 `<name>` - Can be anything, example: National
* `abbrev <abbreviation>` - Makes a GET request and responds with the ID, name, country code, website and wikipedia page of an agency.
`<abbreviation>` - Example: NASA
* `agencyid <id>`: Makes a GET request and responds with the name, country code, website and wikipedia page of the agency. Primarily used to get more information of an agency after acquiring its `<id>` through `agency` or `abbrev`.
* `mission <name>`: Makes a GET request and returns a list with ID's and full names of matches. `<name>` - Can be a part of the full name. Example: Apollo or Insight
* `missionid <id>`: Makes a GET request and returns a missions ID, name and complete description. Primarily used to get more information about a mission after acquiring its `<id>` through `mission`.

*more to come*


### AutoSpace Cog

* `newLaunch`: Background task that checks if there's a new launch every 24 hours from the instant the bot first came online in the guild.
*more to come*

### Fun Cog

Miscellaneous commands (mainly for testing purposes)

`8ball <question>`: Responds randomly to a yes/no question.
`ping`