import discord
import numpy
import random
from discord.ext import commands
#varibles
blacklist = [
"@everyone",
"@here",
"cum",
]
class mod(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
            print("[!]mod cog online")
    @commands.command()
    async def purge(self, ctx, amount=100000):
        await ctx.message.delete()
        embed = discord.Embed(description=f"i have deleted `all` messages", color=ctx.author.color)
        await ctx.channel.purge(limit=amount)
        await ctx.send(embed=embed, delete_after=3)
    @commands.command()
    async def clear(self, ctx, *, amount=5):
        await ctx.message.delete()
        embed = discord.Embed(description=f"i have deleted `{amount}` messages", color=ctx.author.color)
        await ctx.channel.purge(limit=amount)
        await ctx.send(embed=embed, delete_after=3)


    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await ctx.message.delete()
        await member.kick(reason=reason)
        embed = discord.Embed(description=f"{member} has been kicked", color=ctx.author.color)
        await ctx.send(embed=embed, delete_after=3)

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await ctx.message.delete()
        await member.ban(reason=reason)
        embed = discord.Embed(description=f"{member} has been banned", color=ctx.author.color)
        await ctx.send(embed=embed, delete_after=3)
    

def setup(client):
    client.add_cog(mod(client))