import discord
from discord import app_commands
from discord.ext import commands

def help_embed():

    embed = discord.Embed(
        title = "Help Command", description = "This is an embed which will provide you with all the functions available", 
        url = "https://github.com/Abhinav-Achuta/glaze-bot", 
        color = 0xFFC0CB
        )

    embed.set_author(
        name = "glaze bot",
        icon_url = "https://i.imgur.com/rCkUJyG.jpg"
    )

    embed.add_field(
        name = "__Misc. Commands__",
        value = "*List of miscellaneous commands*",
        inline = False
    )

    #Roll command
    embed.add_field(
        name = "!roll (start number) (end number)",
        value = "This command allows you to output a random integer between two numbers you choose from.",
        inline = False
    )

    #Coinflip command
    embed.add_field(
        name = "!coinflip or !coinflip (tts on or off)",
        value = "Flips a coin and gives you heads or tails. If you just say !coinflip will flip a coin and not tts. If you put something after the !coinflip command, tts will be activated.",
        inline = False
    )
    
    #spinwheel command
    embed.add_field(
        name = "!spinwheel (option_1) (option_2) (option_3)",
        value = 'This command will "spin a wheel" and output you the order in which your results landed.\n *if you would like for an option with multiple spaces in the name, surround the phrase with quotes*',
        inline = False
    )

    #Random from list commands
    embed.add_field(
        name = "__List commands__",
        value = "*Commands to create and interact with a list*",
        inline = False
    )

    #Create the list
    embed.add_field(
        name = "!createlist (option_1) (option_2) (option_3)",
        value = "This command will create a list for you that you can use the other commands in this section to interact with\n*if you would like for an option with multiple spaces in the name, surround the phrase with quotes*",
        inline = False
    )

    #Random from list
    embed.add_field(
        name = "!randomfromlist",
        value = "Outputs one random item from the list you created",
        inline = False
    )

    #Show list
    embed.add_field(
        name = "!showlist",
        value = 'Shows you "your list"',
        inline = False
    )

    return embed
