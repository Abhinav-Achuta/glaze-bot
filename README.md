# Glaze-bot: A discord bot with some fun features
## Introduction
This is a bot that has several features made for fun such as spinning wheels, rolling for a random number, coinflipping, and even some features to interact with the Riotgames API to retrieve League of Legends summoner data. This bot is a work in progress and more features will be added (suggestions are welcome).
## About the project
This project uses discord.py and the Riotgames API to function. 
Features that are currently present
- Roll for a value between chosen numbers
- Flip a coin
- Spin a wheel based on chosen data
- Create a list from which you can pull data at random
- Get the win rate(s) of champions played in your last 20 games sorted by win rate
## Installation and steps required to run the project
There are a few things necessary to be able to run and set up your own discord bot. The first is to install the **discord.py** package, the **requests** package, and the **dotenv** package. To install these packages, simply run the following lines in your terminal one at a time.
```
pip install discord.py
```
```
pip install requests
```
```
pip install pip install python-dotenv
```
Once these packages have been created, you will need a discord bot and a riot developer API key to which you will be uploading your code.
1. Discord bot
   - First and foremost, you need to have a [Discord account.](https://discord.com/). Once you have your account, you will need to create a server. 
   - After this step, you will need to go to the [Discord Developer Portal](https://discord.com/developers/docs/intro) and follow the instructions here to create a Discord bot
     - Here you need to create a discord bot with permission to read and send messages. Make sure to save the **key** that will be given here as you will need to use this later
     - Invite the discord bot to your server as this will be your interaction method
2. Riot API key
   - To get your riot developer key, you will need to [sign up as a developer](https://developer.riotgames.com/). After signing up, you will need to follow the steps to get your **key**. Make sure you save this as you will be using this later as well.
3. Dotenv
   - Once you have both of your API keys, download the files from the GitHub page and open up your IDE. Here you will create a file called ".env". In this file, you will have two lines as such:
```
discord_bot_token = TOKEN
riot_api_token = API_KEY
```
  - Where it says token and api_key, plug in the discord bot key and riot API key respectively. This is how your discord bot will get permission to interact with the bot and the Riot Games API for data.
### Discord.py
The discord.py package was used to interact with the Discord API which was used as the user interface This allows for the user to add the bot to their server and request commands by typing in the respective command into their chat box. The discord bot will then act as a user and send back data based on what was requested.
