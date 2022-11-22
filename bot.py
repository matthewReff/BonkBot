import discord
from discord.ext import commands
from discord import Option, ApplicationContext, SlashCommandOptionType
import sys
import json
import requests

API_BASE_URL = "https://testapi.tendec.dev/"
JAIL_ENDPOINT = API_BASE_URL + "v1/jail"
ADD_OFFENSE_ENDPOINT = API_BASE_URL + "v1/addoffense"
RAP_SHEET_ENDPOINT = API_BASE_URL + "v1/rapsheet"

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(intents=intents)

@bot.slash_command(name="jail", guild_only = True, description="Send a user to jail for an offense")
async def jail(
    ctx: ApplicationContext,
    user: Option(SlashCommandOptionType.user, "Who should go to jail"),
    offense: Option(str, "What they should go to jail for")
):
    requestJson = json.dumps(
        {
            "serverId": str(ctx.guild_id),
            "userId": str(user.id),
            "offenseName": offense,
        }
    )
    result = requests.post(JAIL_ENDPOINT, data=requestJson)
    await ctx.respond(f"Got back: {result.status_code} {result.text}")

@bot.slash_command(name="addoffense", guild_only = True, description="Add a new jailable offense")
async def addOffense(
    ctx: ApplicationContext,
    offense: Option(str, "Name of the offense you want to add")
):
    requestJson = json.dumps(
        {
            "serverId": str(ctx.guild_id),
            "offenseName": offense,
        }
    )
    result = requests.put(ADD_OFFENSE_ENDPOINT, data=requestJson)

    await ctx.respond(f"Got back: {result.status_code} {result.text}")


@bot.slash_command(name="rapsheet", guild_only = True, description="Get a list of offenses for the user")
async def rapSheet(
    ctx: ApplicationContext,
    user: Option(SlashCommandOptionType.user, "Whose rapsheet to find")
):
    requestJson = json.dumps(
        {
            "serverId": str(ctx.guild_id),
            "userId": str(user.id),
        }
    )
    result = requests.post(RAP_SHEET_ENDPOINT, data=requestJson)

    await ctx.respond(f"Got back: {result.status_code}, {result.text}")
    
if len(sys.argv) != 2:
    print("You need to provide the bot token when you startup the bot")
    exit()

botToken = sys.argv[1]
bot.run(botToken)