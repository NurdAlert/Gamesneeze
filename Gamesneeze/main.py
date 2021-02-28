import discord; from discord.ext import commands
import motor.motor_asyncio
from globals import get_from_cfg
from colorama import Style, Back, Fore

# Variables.
username = get_from_cfg(section="Connection Info", key="mongo_username")
password = get_from_cfg(section="Connection Info", key="mongo_password")
token = get_from_cfg(section="Connection Info", key="token")

# Important Starting Code.
print(f"Username: {username}\n Password: {password}\n Token: {token}")
mongo_client = motor.motor_asyncio.AsyncIOMotorClient(f"mongodb+srv://{username}:{password}@gamesneezecluster.snsd8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
client = commands.Bot(command_prefix='gs!')

# Removing Default Help Command.

client.remove_command('help')

# Defining Commands.

@client.command()
async def sneeze(ctx, member : discord.Member=None):

    if member == None:
        await ctx.send(f"{ctx.author.mention} Sneezed!")

    elif member != None:
        await ctx.send(f"{ctx.author.mention} Sneezed On {member.mention}")

    print(f"{ctx.author} Used Sneeze In {ctx.guild.name}")

@client.command()
async def help(ctx, command : str=None):

    pass










# All Events.

@client.event
async def on_command_error(ctx, error):

    await ctx.send(f"```fix\n[INTERNAL ERROR]:```\n```{error}```")
    print(Fore.RED, error)

@client.event
async def on_ready():
    print("Sneezing On Gamers...")
client.run(token)

