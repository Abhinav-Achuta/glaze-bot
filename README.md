# [Glaze-bot: Your Competitive analysis Discord Ally for Gamers](https://github.com/Abhinav-Achuta/glaze-bot/)

## Introduction
Greetings, League of Legends enthusiasts! I'm Glaze, a versatile bot with a plethora of features to enhance your gaming experience. Indulge in a spin of the wheel, roll for a random number, or toss a virtual coin to test your luck. For the avid Summoners among you, I've tapped into the Riotgames API to provide insights into your League of Legends adventures. Explore your summoner data, delve into champion statistics, and discover strategies to dominate the Rift. I'm continuously evolving, so feel free to suggest new features to elevate this bot's capabilities. Let's embark on an exciting journey together!

## About the project
This project uses discord.py and the Riotgames API to function. 

Want to improve your performance on the rift?
- Use the Riotgames API to delve into your summoner data
- Uncover hidden insights into your champion statistics and make informed decisions on who to play

Conflicted on what decision to make?
- Spin the wheel of fortune and let destiny decide your next move
- Toss a virtual coin and leave it up to chance
- Roll for a random number and leave it up to fate

I'm continuously evolving and eager to incorporate your feedback and suggestions. Share your ideas and let's shape this bot into the ultimate gaming companion.

## Installation and steps required to run the project
There are a few things necessary to be able to run and set up your own Discord bot. The first is to install the **discord.py** package, the **requests** package, and the **dotenv** package. To install these packages, simply run the following lines in your terminal one at a time.
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
   - First and foremost, you need to have a [Discord account](https://discord.com/). Once you have your account, you will need to create a server. 
   - After this step, you will need to go to the [Discord Developer Portal](https://discord.com/developers/docs/intro) and follow the instructions here to create a Discord bot
     - Here you need to create a discord bot with permission to read and send messages. Make sure to save the **key** that will be given here as you will need to use this later
     - Invite the discord bot to your server as this will be your interaction method
2. Riot API key
   - To get your riot developer key, you will need to [sign up as a developer](https://developer.riotgames.com/). After signing up, you will need to follow the steps to get your **key**. Make sure you save this as you will be using this later as well.
3. Dotenv
   - Once you have both of your API keys, download the files from the GitHub page and open up your IDE. Here you will create a file called ".env". In this file, you will write two lines as such replacing the words TOKEN and API_KEY with your discord bot token and Riot Games API key respectively:
```
discord_bot_token = TOKEN
riot_api_token = API_KEY
```
## Running the bot
To run the bot, you simply have to run the main.py python file. This will start up the discord bot from which you can now use the commands available. To get a list of what commands are available, all you need to do is type in "!help" or "/help" in the chat box and send your message. There will be a list of commands and the syntax that should be followed that shows up.
I recommend running the bot on a server such as the Google Cloud so the discord bot can be available for use at all times.

## Packages involved
### Discord.py
The discord.py package was used to interact with the Discord API which was used as the user interface This allows for the user to add the bot to their server and request commands by typing in the respective command into their chat box. The discord bot will then act as a user and send back data based on what was requested. The usage of discord.py allows for easy interaction with the discord API and allows for the formatting of messages as well as data collection from the user that can then be processed in the background.

### Dotenv
This package allows for both Discord token and riot API token to be hidden from the public eye. It will be stored locally so other people can not use your keys for nefarious purposes.

### Requests
This is a package that allows the user to send "requests" online for data. In this project, it was used to interact with the Riot Games API for data collection purposes. Based on the user's username and tagline, the project can request match data for that specific individual. While the data that is given back has many stats the only data that is currently looked at is champion data, number of wins, and games played to calculate the win rate per champion.

## Design of packages, classes, methods, functions, and iterations between them
When a command is called in the discord server using the "!" key, the discord bot (using discord.py) will read the message and cross reference with code in the bot.py file. If there is command available that has the same syntax as the entered command, the code will then process the data to perform the requested function by communicating with other files within the parent directory as necessary. For example, if the command "!lolwr Naoki abhi" is called, the code will then receive "Naoki" and "abhi" as data for the !lolwr command. This command will follow the following pathway
1. Enable the Riot games key to be used in the LOL_sort_games_wr.py file.
2. Request data using the requests package to receive data for the user Naoki#abhi
3. Request match data for the same user
4. Look through each match to pull data specific to the user
5. Sort the data from highest to lowest using bubble sort
6. Send data back to the bot.py file
7. Format the data using the embed feature available in discord.py
8. Send the data back to the user through the discord server
All the commands will follow a path of sorts communicating with necessary files to return the information requested. The data is stored in a combination of lists, dictionaries, and classes for data processing.

## Current expected weaknesses
While the discord bot works amazingly overall, the only known weakness as of now is the time it takes for the "!lolwr" command. This command takes about 10 seconds to fully finish as it has to request data multiple different times from the Riot Games API to procure all necessary information. This data then has to be processed which doesn't take much time but still adds to the time taken for the command.

## Data structures and algorithms used
- Lists
   - Can be seen throughout all the code as they are used for data sorting
- Dictionaries
   - Can be seen throughout the code as they are used for data sorting and collection
- Classes
   - Can be seen in the LOL_sort_games_wr.py file. The class "Champion" was created to help store data collected from the Riot Games API in a usable manner.
- Bubble sort
   - This algorithm was used in the LOL_sort_games_wr.py file to sort the Champion data by win rates in order from greatest to lowest
