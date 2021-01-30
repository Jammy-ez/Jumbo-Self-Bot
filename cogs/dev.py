import discord
import random
from discord.ext import commands
import time
#varibles

class dev(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
            print("[!]dev cog online")
    @commands.command()
    async def botdev(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(description=f"Jam made this bot, if any devs also help this message will be updated with there profiles", color=ctx.author.color)
        await ctx.send(embed=embed)
        time.sleep(1)
        embed1 = discord.Embed(description=f"Jam: Jam#4613", color=ctx.author.color)
        await ctx.send(embed=embed1)

    @commands.command()
    async def invite(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(description=f"https://discord.com/api/oauth2/authorize?client_id=800050256393535502&permissions=8&scope=bot", color=ctx.author.color)
        await ctx.send(embed=embed)
def setup(client):
    client.add_cog(dev(client))