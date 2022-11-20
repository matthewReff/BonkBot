import discord
from discord.ext import commands
from discord import Option, ApplicationContext, SlashCommandOptionType
import sys

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(intents=intents)

@bot.slash_command(name="jail", guild_only = True, description="Send a user to jail for an offense")
async def jail(
    ctx: ApplicationContext,
    user: Option(SlashCommandOptionType.user, "Who should go to jail"),
    offense: Option(str, "What they should go to jail for")
):
    await ctx.respond(f"{user.id} {offense} {ctx.guild_id}")

@bot.slash_command(name="addoffense", guild_only = True, description="Add a new jailable offense")
async def addOffense(
    ctx: ApplicationContext,
    offense: Option(str, "Name of the offense you want to add")
):
    await ctx.respond(f"{offense} {ctx.guild_id}")

@bot.slash_command(name="rapsheet", guild_only = True, description="Get a list of offenses for the user")
async def rapSheet(
    ctx: ApplicationContext,
    user: Option(SlashCommandOptionType.user, "Whose rapsheet to find")
):
    await ctx.respond(f"{user.id} {ctx.guild_id}")
    
if len(sys.argv) != 2:
    print("You need to provide the bot token when you startup the bot")
    exit()

botToken = sys.argv[1]
bot.run(botToken)