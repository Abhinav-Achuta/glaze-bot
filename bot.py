import discord
from discord import app_commands
from discord.ext import commands

#importing other python files
import responses
import help_response

#Importing token/api keys
from dotenv import load_dotenv
import os

#Test
def configure():
    load_dotenv()

def run_discord_bot():

    TOKEN = os.getenv("discord_bot_token")

    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix = "!", intents = intents)

    #Slash Command test
    @bot.event
    async def on_ready():
        print("Bot is Up and Ready!")

        try:
            synced = await bot.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(e)
    
    #Hello command
    @bot.tree.command(name = "hello")
    async def hello(interaction: discord.Interaction):
        await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a /command!", ephemeral = True)

    #Help commands

    @bot.tree.command(name = "help")
    async def help(interaction: discord.Interaction):

        #command user info
        requester = interaction.user
        requester_picture = interaction.user.display_avatar

        #adding footer to embed
        embed = help_response.help_embed()
        embed.set_footer(
            text = f"Requested By: @{requester}",
            icon_url = requester_picture
        )

        await interaction.response.send_message(content = requester.mention,embed=embed, ephemeral=False)

    bot.remove_command("help") #Remove the old help command

    @bot.command()
    async def help(ctx):
        embed = help_response.help_embed()

        #command user info
        requester = ctx.author
        requester_picture = ctx.author.avatar

        #adding footer to embed
        embed = help_response.help_embed()
        embed.set_footer(
            text = f"Requested By: @{requester}",
            icon_url = requester_picture
        )

        await ctx.send(content = requester.mention ,embed = embed) #Sends message back to channel

    #Roll random number
    @bot.command()
    async def roll(ctx, num_1, num_2):
        await ctx.send(responses.roll(num_1, num_2))

    #Flip a coin
    @bot.command()
    async def coinflip(ctx, msg = None):

        output_text, tts_on_or_off = responses.coinflip(msg)

        await ctx.send(f"{output_text}", tts = tts_on_or_off)

    #Spin a wheel
    @bot.command()
    async def spinwheel(ctx, *args):
        user = ctx.author
        await ctx.send(responses.spin_wheel(args, user))

    #Choose random values from a list
    random_dict = {}

    @bot.command()
    async def createlist(ctx, *args):
        user = ctx.author
        user_input = responses.make_options_into_list(args)

        random_dict[user] = user_input

        await ctx.send("Your list was created. If you would like to chose an item at random from the list (will be removed) please type in '!randomfromlist'\n"
                       f"Your list: {random_dict[user]}")

    @bot.command()
    async def randomfromlist(ctx):
        user = ctx.author
        output_string, need_to_delete = responses.random_from_list(random_dict, user)

        if need_to_delete != None:
            del random_dict[user][need_to_delete]

        await ctx.send(output_string)

    @bot.command()
    async def showlist(ctx):
        user = ctx.author
        await ctx.send(responses.show_list(random_dict, user))

    @bot.command()
    async def addtolist(ctx, *args):
        user = ctx.author
        user_input = responses.make_options_into_list(args)

        if user not in random_dict:
            random_dict[user] = []

        for i in range(len(user_input)):
            random_dict[user].append(user_input[i])

        await ctx.send(f"Your option(s) were added!\nYour list: {random_dict[user]}")

    @bot.command()
    async def removefromlist(ctx, *args):
        user = ctx.author
        user_input = responses.make_options_into_list(args)

        if user not in random_dict:
            random_dict[user] = []

        for item in user_input:
            if item in random_dict[user]:
                del random_dict[user][item]

        if random_dict[user] == []:
            await ctx.send(f"The items in your list were removed it is now empty.")
        else:
            await ctx.send(f"The items you requested were removed from your list.\nYour list: {random_dict}")
    
    @bot.command()
    async def clearlist(ctx):
        user = ctx.author

        random_dict[user] = []

        await ctx.send("Your list was cleared!")


    #Runs the bot
    bot.run(TOKEN)