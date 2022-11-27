import discord
from discord.ext import commands
from discord import Option, ApplicationContext, SlashCommandOptionType
import sys

from api.bonkApi import *

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(intents=intents)

@bot.slash_command(name="jail", guild_only = True, description="Send a user to jail for an offense")
async def jail(
    ctx: ApplicationContext,
    user: Option(SlashCommandOptionType.user, "Who should go to jail"),
    offense: Option(str, "What they should go to jail for")
):
    resultOrError = jailCall(ctx.guild_id, user.id, offense)
    await debugLogResultOrError(ctx, resultOrError)

@bot.slash_command(name="addoffense", guild_only = True, description="Add a new jailable offense")
async def addOffense(
    ctx: ApplicationContext,
    offense: Option(str, "Name of the offense you want to add")
):
    resultOrError = addOffenseCall(ctx.guild_id, offense)
    await debugLogResultOrError(ctx, resultOrError)

@bot.slash_command(name="rapsheet", guild_only = True, description="Get a list of offenses for the user")
async def rapSheet(
    ctx: ApplicationContext,
    user: Option(SlashCommandOptionType.user, "Whose rapsheet to find")
):
    resultOrError = rapsheetCall(ctx.guild_id, user.id)
    await debugLogResultOrError(ctx, resultOrError)

@bot.slash_command(name="getoffenses", guild_only = True, description="Get the list of valid offenses for the server")
async def getOffenses(
    ctx: ApplicationContext
):
    resultOrError = getOffensesCall(ctx.guild_id)
    await debugLogResultOrError(ctx, resultOrError)

@bot.event
async def on_ready():
    print(f'{bot.user} is online.')

if len(sys.argv) != 2:
    print("You need to provide the bot token when you startup the bot")
    exit()

async def debugLogResultOrError(ctx, resultOrError):
    message = f"Succeeded: {resultOrError.isSuccess()}"
    if resultOrError.result != None:
        message += "\n"
        message += f"result: {json.dumps(resultOrError.result)}"
    if resultOrError.error != None:
        message += "\n"
        message += f"error: {resultOrError.error.status} {resultOrError.error.message}"
    await ctx.respond(message)

botToken = sys.argv[1]
bot.run(botToken)