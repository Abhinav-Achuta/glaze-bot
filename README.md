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
### Discord.py
The discord.py package was used to interact with the Discord API which was used as the user interface This allows for the user to add the bot to their server and request commands by typing in the respective command into their chat box. The discord bot will then act as a user and send back data based on what was requested.
