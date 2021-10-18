import discord
from discord.ext import commands

class registrasi_g3(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def Perkenalan_yuk(self, ctx, *data):
        data = list(data)
        for x, y in enumerate(data):
            data[x] = y.lower()
        if "science" in data or "science." in data:
            role = discord.utils.get(ctx.guild.roles, name = "Data Science")
            await ctx.author.add_roles(role)
        else:
            role = discord.utils.get(ctx.guild.roles, name = "Data Engineering")
            await ctx.author.add_roles(role)
            
        if "project" in data or "project." in data:
            role = discord.utils.get(ctx.guild.roles, name = "Project")
            await ctx.author.add_roles(role)
        elif "research" in data or "research." in data or "riset" in data or "riset." in data:
            role = discord.utils.get(ctx.guild.roles, name = "Research")
            await ctx.author.add_roles(role)
        elif "community" in data or "community." in data or "pengabdian" in data or "pengabdian." in data:
            role = discord.utils.get(ctx.guild.roles, name = "Community Service")
            await ctx.author.add_roles(role)

        role_default1 = discord.utils.get(ctx.guild.roles, name = "EDE Trooper")
        await ctx.author.add_roles(role_default1)
        
        role_default2 = discord.utils.get(ctx.guild.roles, name = "G3")
        await ctx.author.add_roles(role_default2)

def setup(client):
    client.add_cog(registrasi_g3(client))