import discord
from discord.ext import commands
import sys

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(intents=intents)

@bot.slash_command(name="first_slash", guild_ids=['467887610124042240']) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_slash(ctx): 
    await ctx.respond("You executed the slash command!")
    
if len(sys.argv) != 2:
    print("You need to provide the bot token when you startup the bot")
    exit()

botToken = sys.argv[1]
bot.run(botToken)