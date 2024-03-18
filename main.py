import json
import discord
from discord.ext import commands
import tls_client

client = commands.Bot(command_prefix = ';', intents=discord.Intents.all())

with open('config.json', 'r') as file:
    config = json.load(file)
bot_token = config['bot_token']

@client.event
async def on_ready():
    print(f"bot is online {client.user}")
    
@client.command()
async def check(ctx, *, tken:str):
    session = tls_client.Session(client_identifier="chrome_120", random_tls_extension_order=True)
    session.headers = {
        "authorization":
        tken
        }
    response = session.get('https://discord.com/api/v9/users/@me')
    if response.status_code == 401:
        await ctx.send("token is invalid")
    else:
     respo = response.json()
    await ctx.send("```\n%s\n```" % json.dumps(respo, indent=4))

client.run(bot_token, reconnect=True)