import discord
from discord.ext import commands
from discord import Option, ApplicationContext, SlashCommandOptionType
import sys

from api.bonkApi import *

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(intents=intents)

@bot.slash_command(name="jail", guild_only = True, description="Send a user to jail for an offense")
async def jailSlashCommand(
    ctx: ApplicationContext,
    user: Option(SlashCommandOptionType.user, "Who should go to jail"),
    offense: Option(str, "What they should go to jail for")
):
    resultOrError = jailCall(ctx.guild_id, user.id, offense)
    if resultOrError.isFailure():
        await ctx.respond("Unknown error")
    rapsheetString = await getRapsheetString(ctx, user)
    await ctx.respond(f"Sent {user.name} to jail for {offense}" + "\n" + rapsheetString)

@bot.slash_command(name="addoffense", guild_only = True, description="Add a new jailable offense")
async def addOffenseSlashCommand(
    ctx: ApplicationContext,
    offense: Option(str, "Name of the offense you want to add")
):
    resultOrError = addOffenseCall(ctx.guild_id, offense)
    if resultOrError.isFailure():
        await ctx.respond("Unknown error")
    offenseListString = await getOffenseListString(ctx)
    await ctx.respond(f"Added {offense} as a possible offense" + "\n" + offenseListString)

@bot.slash_command(name="rapsheet", guild_only = True, description="Get a list of offenses for the user")
async def rapSheetSlashCommand(
    ctx: ApplicationContext,
    user: Option(SlashCommandOptionType.user, "Whose rapsheet to find")
):
    await ctx.respond(await getRapsheetString(ctx, user))

@bot.slash_command(name="listoffenses", guild_only = True, description="Get the list of valid offenses for the server")
async def listOffensesSlashCommand(
    ctx: ApplicationContext
):
    await ctx.respond(await getOffenseListString(ctx))

async def getOffenseListString(ctx):
    resultOrError = getOffensesCall(ctx.guild_id)
    if resultOrError.isFailure():
        await ctx.respond("Unknown error")

    offenseList = resultOrError.result["offenses"]
    return offenseList.join(",")

async def getRapsheetString(ctx, user):
    resultOrError = rapsheetCall(ctx.guild_id, user.id)
    if resultOrError.isFailure():
        await ctx.respond("Unknown error")

    rapsheet = resultOrError.result["rapSheet"]

    returnString = ""
    for offenseName in rapsheet.keys():
        offenseCount = rapsheet.get(offenseName)
        returnString += offenseName + " : " + offenseCount + "\n";
    return returnString

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