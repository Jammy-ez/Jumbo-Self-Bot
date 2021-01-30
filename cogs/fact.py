import discord
import random
from discord.ext import commands
import requests
import urllib
from aiohttp import request
#varibles
DOG_FACT = "https://some-random-api.ml/facts/dog"
CAT_FACT = "https://some-random-api.ml/facts/cat"
class fact(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
            print("[!]fact cog online")

    @commands.command()
    async def dog_fact(self, ctx):
        await ctx.message.delete()
        async with request("GET", DOG_FACT, headers=[]) as response:
            if response.status == 200:
                data = await response.json()
                embed = discord.Embed(description=data["fact"], color=ctx.author.color)
                await ctx.send(embed=embed)

    @commands.command()
    async def cat_fact(self, ctx):
        await ctx.message.delete()
        async with request("GET", CAT_FACT, headers=[]) as response:
            if response.status == 200:
                data = await response.json()
                embed = discord.Embed(description=data["fact"], color=ctx.author.color)
                await ctx.send(embed=embed)

def setup(client):
    client.add_cog(fact(client))