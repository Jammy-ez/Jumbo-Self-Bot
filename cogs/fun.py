import requests
import urllib
from aiohttp import request
import discord
import random
from discord.ext import commands
import time
#varibles
magic8ball_respond = [
"It is certain.",
"It is decidedly so.",
"Without a doubt.",
"Yes - definitely.",
"You may rely on it.",
"As I see it, yes.",
"Most likely.",
"Outlook good.",
"Yes.",
"Signs point to yes.",
"Reply hazy, try again.",
"Ask again later.",
"Better not tell you now.",
"Cannot predict now.",
"Concentrate and ask again.",
"Don't count on it.",
"My reply is no.",
"My sources say no.",
"Outlook not so good.",
"Very doubtful."]
dick_respond = [
"8=D",
"8==D",
"8===D",
"8====D",
"8=====D",
"8======D",
"8=======D",
"8========D",
"8=========D",
"8==========D",
"8===========D",
"8============D",
"8=============D",
"8==============D",
"8===============D",
"8================D",
"8=================D",
"8==================D",
"8===================D",
"8====================D",
"8=====================D",
"8======================D",
"8=======================D",
"8========================D",
"8=========================D",
"8==========================D",
"8===========================D",
"8============================D Packing lmao",
"8D no dock",
"8-D",
"8--D",
"8---D",
"8----D",
"8-----D",
"8------D",
"8-------D",
"8--------D",
"8---------D",
"8----------D",
"8-----------D",
"8------------D",
"8-------------D",
"8--------------D",
"8---------------D",
"8----------------D",
"8-----------------D",
"8------------------D",
"8-------------------D",
"8--------------------D",
"8---------------------D",
"8----------------------D",
"8-----------------------D",
"8------------------------D",
"8-------------------------D",
"8--------------------------D",
"8---------------------------D",
"8----------------------------D Packing lmao",
"o=D one ball",
]
class fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
            print("[!]fun cog online")

    @commands.command(aliases=["8ball"])
    async def magic_ball(self, ctx, *, question):
        await ctx.message.delete()
        answer = random.choice(magic8ball_respond)
        embed = discord.Embed()
        embed.add_field(name="Question", value=question, inline=False)
        embed.add_field(name="Answer", value=answer, inline=False)
        embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
        await ctx.send(embed=embed)

    @commands.command()
    async def dick(self, ctx, *, member):
        await ctx.message.delete()
        embed = discord.Embed(description=f"User: {member} Dick: {random.choice(dick_respond)} ", color=ctx.author.color)
        await ctx.send(embed=embed)

    @commands.command()
    async def say(self, ctx, *, word):
        await ctx.message.delete()
        embed = discord.Embed(description=f"{word}", color=ctx.author.color)
        await ctx.send(embed=embed)

    @commands.command()
    async def spam(self, ctx, *, word, times=50):
        await ctx.message.delete()
        embed = discord.Embed(description=f"{word}", color=ctx.author.color)
        for i in range(0,int(times)):
            time.sleep(1)
            await ctx.send(embed=embed)
    @commands.command()
    async def ascii(self, ctx, *, text):
        await ctx.message.delete()
        r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
        if len('```'+r+'```') > 2000:
            return
        await ctx.send(f"```{r}```")

def setup(client):
    client.add_cog(fun(client))