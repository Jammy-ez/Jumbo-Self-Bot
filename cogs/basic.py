import discord
from discord.ext import commands
#varibles
JumboPic = "https://cdn.discordapp.com/attachments/795757273153929220/803993863483424828/logo.jpg"
class basic(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
            print("[!]basic cog online")

    @commands.command()
    async def pong(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(description=f"Ping! `{round(self.client.latency * 1000)}ms`", color=ctx.author.color)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def nsfw(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(color=ctx.author.color)
        embed.add_field(name="Hentai", value="\npic/Gif of hentai", inline=False)
        embed.add_field(name="Belle_delphine", value="\nPic/gif of bell delphine", inline=False)
        embed.add_field(name="hentai_gif", value="\nGif of hentai", inline=False)
        embed.add_field(name="Anal", value="\nPic/gif of anal", inline=False)
        embed.add_field(name="Feet", value="\nPic/gif of Feet", inline=False)
        embed.add_field(name="Boobs", value="\nPic/gif of boobs", inline=False)
        embed.add_field(name="Pussy", value="\nPic/gif of pussy", inline=False)
        embed.add_field(name="Blowjob", value="\nPic/gif of Blowjobs", inline=False)
        embed.add_field(name="Lesbian", value="\nPic/gif of lesbians", inline=False)
        embed.set_thumbnail(url=JumboPic)
        await ctx.send(embed=embed)

    @commands.command()
    async def help(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(color=ctx.author.color)
        embed.add_field(name="Basic", value="\nBasic commands", inline=False)
        embed.add_field(name="Fun", value="\nFun commands", inline=False)
        embed.add_field(name="Image", value="\nImage commands", inline=False)
        embed.add_field(name="fact", value="\nFact commands", inline=False)
        embed.add_field(name="Nsfw", value="\nNsfw commands", inline=False)
        embed.add_field(name="Mod", value="\nMod commands", inline=False)
        embed.add_field(name="Dev", value="\nDev commands", inline=False)
        embed.set_thumbnail(url=JumboPic)
        await ctx.send(embed=embed)
    @commands.command()
    async def fun(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(color=ctx.author.color)
        embed.add_field(name="8ball", value="\nAnswers your question", inline=False)
        embed.add_field(name="Dick", value="\nDick", inline=False)
        embed.add_field(name="Ascii", value="\nAscii art of text", inline=False)
        embed.add_field(name="Say", value="\nSays whatever you say", inline=False)
        embed.add_field(name="Spam", value="\nSpams whatever you say", inline=False)
        embed.set_thumbnail(url=JumboPic)
        await ctx.send(embed=embed)
    @commands.command()
    async def image(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(color=ctx.author.color)
        embed.add_field(name="Dog_img", value="\nImage of dog", inline=False)
        embed.add_field(name="Cat_img", value="\nImage of cat", inline=False)
        embed.add_field(name="Meme", value="\nImage of meme", inline=False)
        embed.add_field(name="Wink", value="\nWink gifl", inline=False)
        embed.add_field(name="Hug", value="\nHug gif", inline=False)
        embed.add_field(name="Oreo_img", value="\nImage of an oreo", inline=False)
        embed.add_field(name="Jam_img", value="\nImage of bot dev", inline=False)
        embed.add_field(name="Noodle_img", value="\nImage of noodle", inline=False)
        embed.set_thumbnail(url=JumboPic)
        await ctx.send(embed=embed)
    @commands.command()
    async def fact(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(color=ctx.author.color)
        embed.add_field(name="Dog_fact", value="\nDog fact", inline=False)
        embed.add_field(name="Cat_fact", value="\nCat fact", inline=False)
        embed.set_thumbnail(url=JumboPic)
        await ctx.send(embed=embed)

    @commands.command()
    async def mod(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(color=ctx.author.color)
        embed.add_field(name="Bans", value="\nBans mentioned user", inline=False)
        embed.add_field(name="kick", value="\nKicks mentioned user", inline=False)
        embed.add_field(name="purge", value="\nNukes chat", inline=False)
        embed.add_field(name="Clear", value="\nClears chat on the ammount u want", inline=False)
        embed.set_thumbnail(url=JumboPic)
        await ctx.send(embed=embed)
    @commands.command()
    async def dev(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(color=ctx.author.color)
        embed.add_field(name="Botdev", value="\nBot developer", inline=False)
        embed.add_field(name="Invite", value="\nInvite of bot", inline=False)
        embed.set_thumbnail(url=JumboPic)
        await ctx.send(embed=embed)
    @commands.command()
    async def nuke(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(color=ctx.author.color)
        embed.add_field(name="Dm_clear", value="\nClear schat with white space", inline=False)
        embed.add_field(name="Channel_delete", value="\nDelets all channels", inline=False)
        embed.add_field(name="Role_spam", value="\nSpams roles", inline=False)
        embed.add_field(name="Role_delete", value="\ndeletes all roles", inline=False)
        embed.add_field(name="Ban_all", value="\nBans_all", inline=False)
        embed.add_field(name="Destroy", value="\nDeletes everything", inline=False)
        embed.set_thumbnail(url=JumboPic)
        await ctx.send(embed=embed)
def setup(client):
    client.add_cog(basic(client))