import discord
from discord.ext import commands
from discord import Option, ApplicationContext, SlashCommandOptionType
import sys
import json
import requests

from bonkApi import *

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(intents=intents)

@bot.slash_command(name="jail", guild_only = True, description="Send a user to jail for an offense")
async def jail(
    ctx: ApplicationContext,
    user: Option(SlashCommandOptionType.user, "Who should go to jail"),
    offense: Option(str, "What they should go to jail for")
):
    result = jailCall(ctx.guild_id, user.id, offense)
    await ctx.respond(f"Got back: {result.status_code} {result.text}")

@bot.slash_command(name="addoffense", guild_only = True, description="Add a new jailable offense")
async def addOffense(
    ctx: ApplicationContext,
    offense: Option(str, "Name of the offense you want to add")
):
    result = addOffenseCall(ctx.guild_id, offense)
    await ctx.respond(f"Got back: {result.status_code} {result.text}")


@bot.slash_command(name="rapsheet", guild_only = True, description="Get a list of offenses for the user")
async def rapSheet(
    ctx: ApplicationContext,
    user: Option(SlashCommandOptionType.user, "Whose rapsheet to find")
):
    result = rapsheetCall(ctx.guild_id, user.id)
    await ctx.respond(f"Got back: {result.status_code}, {result.text}")

@bot.slash_command(name="getoffenses", guild_only = True, description="Get the list of valid offenses for the server")
async def getOffenses(
    ctx: ApplicationContext
):
    result = getOffensesCall(ctx.guild_id)
    await ctx.respond(f"Got back: {result.status_code}, {result.text}")

@bot.event
async def on_ready():
    print(f'{bot.user} is online.')

if len(sys.argv) != 2:
    print("You need to provide the bot token when you startup the bot")
    exit()

    
botToken = sys.argv[1]
bot.run(botToken)