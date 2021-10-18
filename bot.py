from discord.ext import commands
import discord
import os
# bot EDE aslinya pake EDE!
client = commands.Bot(command_prefix = "tes!")

token = ""

@client.event
async def on_ready():
    #This App Grows
    name = 'This App Debug'
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=name))
    print("We have logged in as {}".format(client.user))

@client.command()
async def ping(ctx):
    ping = str(round(client.latency * 100)) + " ms"
    embed=discord.Embed(color=0xffa200)
    embed.add_field(name="Ping " + str(ctx.author), value=ping, inline=False)
    await ctx.send(embed=embed)

@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

if __name__ == "__main__":
    client.run(token)