Astroboy
=========

A discord bot that notifies of upcoming launches by various space agencies every 24 hours with additional commands. This bot uses  [NASA's API](https://api.nasa.gov/), [Launchlibrary's API](https://launchlibrary.net/docs/1.4/api.html) and [Open Notify's API](http://open-notify.org/Open-Notify-API/People-In-Space/).

Requires Python `3.5.3` or higher as it uses [discord.py](https://github.com/Rapptz/discord.py) version `1.1.1` 

## Instructions
1. `python -m pip install requirements.txt` to install necessary packages.  
2. Replace "token" with your bot's token in `credentials.json`.  
3. Replace "nasa_api_key" with your api key in `credentials.json`. You can get your key in an instant from [NASA's page](https://api.nasa.gov/index.html#apply-for-an-api-key). 
4. Run `bot.py`. That's all!  

**Prefixes**: 
* $ 
* .

## Commands

### Bot 
* `close`: Closes the bot and logs out all instances.
* `load <extension>`: Manually loads a cog through its name `<extension>`.
* `unload <extension>`: Manually unloads a cog through its name `<extensions>`.
* `reset <extension>`: Unloads and loads a cog to refresh any changes made.

### AutoSpace Cog (commands that run periodically)
* `newLaunch`: Background task that checks if there's a new launch every 24 hours from the instant the bot first came online in the guild.
* `apod`: Background task that messages the current Astronomy Picture of the Day through NASA's API.

### ManualSpace Cog (Commands that need to be invoked)
<<<<<<< HEAD
* `pos`: Makes a GET request and responds with the number of people currently in space, their names and the spacecraft they're on.
=======
>>>>>>> 4f9874cd46a61fcfe79d503265966bfc73009a22
* `apod`: Makes a GET request and responds with information about the Astronomy Picture Of the Day.
* `nextlaunch`: Makes a GET request and responds with the next upcoming launch's name, location, launch window and stream link.
* `rocket <name>`: Makes a GET request and responds with the ID and full name of a rocket through its `<name>`.
* `rocketid <id>`: Makes a GET reqeust and reponds with the ID, full name, agencies involved, information URL and an image. Primarily used to get more information of a rocket after acquiring its `<id>` through `<rocket>`.
* `agency <name>`: Makes a GET request and returns a list of all the matches' ID, full name and abbreviation.
 `<name>` - Can be anything, example: National
* `abbrev <abbreviation>` - Makes a GET request and responds with the ID, name, country code, website and wikipedia page of an agency.
`<abbreviation>` - Example: NASA
* `agencyid <id>`: Makes a GET request and responds with the name, country code, website and wikipedia page of the agency. Primarily used to get more information of an agency after acquiring its `<id>` through `agency` or `abbrev`.
* `mission <name>`: Makes a GET request and returns a list with ID's and full names of matches. `<name>` - Can be a part of the full name. Example: Apollo or Insight
* `missionid <id>`: Makes a GET request and returns a missions ID, name and complete description. Primarily used to get more information about a mission after acquiring its `<id>` through `mission`.

### Fun Cog (Miscellaneous commands)(Mainly for testing purposes)
`8ball <question>`: Responds randomly to a yes/no question.  
`ping`: Replies with pong.
