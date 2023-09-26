import discord
from discord import app_commands
from discord.ext import commands
import responses
from dotenv import load_dotenv
import os

#Test
def configure():
    load_dotenv()

def run_discord_bot():

    TOKEN = os.getenv("discord_bot_token")
    print(TOKEN)

    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix = "!", intents = intents)

    #/Command test
    @bot.event
    async def on_ready():
        print("Bot is Up and Ready!")

        try:
            synced = await bot.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(e)
    
    @bot.tree.command(name = "hello")
    async def hello(interaction: discord.Interaction):
        await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a /command!", ephemeral = True)

    #Help command
    @bot.command()
    async def plzhelp(ctx):
        await ctx.send(responses.help_message()) #Sends message back to channel

    #Roll random number
    @bot.command()
    async def roll(ctx, num_1, num_2):
        await ctx.send(responses.roll(num_1, num_2))

    #Flip a coin
    @bot.command()
    async def coinflip(ctx):
        await ctx.send(responses.coinflip())

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


    #Runs the bot
    bot.run(TOKEN)