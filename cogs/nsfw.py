import discord
import random
from discord.ext import commands
import requests
import urllib
from aiohttp import request
#varibles
pussyurl = "https://nekos.life/api/v2/img/pussy"
lesurl = "https://nekos.life/api/v2/img/les"
blowjoburl = "https://nekos.life/api/v2/img/blowjob"
booburl = "https://nekos.life/api/v2/img/boobs"
hentaiurl = "https://nekos.life/api/v2/img/Random_hentai_gif"
feeturl = "https://nekos.life/api/v2/img/feetg"
analurl = "https://nekos.life/api/v2/img/anal"
hentaidp = [
"https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Hentai_-_yuuree-redraw.jpg/220px-Hentai_-_yuuree-redraw.jpg",
"https://img-hw.xvideos-cdn.com/videos/thumbs169lll/08/b8/9d/08b89dad2557e13d76734a8b1905a614/08b89dad2557e13d76734a8b1905a614.29.jpg",
"https://www.hentaimovie.tv/wp-content/uploads/2018/06/3736.jpg",
"https://hentaipussypics.com/blog/wp-content/uploads/2020/07/chika-hentai-13.jpg",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2ERxVfnxXkZTRw_pTtcU7RT82l62L1357sw&usqp=CAU",
"https://hentaigasm.tv/wp-content/uploads/2020/09/Succubus-Stayed-Life-The-Animation-Episode-1.jpg",
"https://grid.fapster.xxx/contents/videos_screenshots/116000/116174/preview.jpg",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGAI7gxdPfZgqYotCNA4JvPPSrC85rS4utLw&usqp=CAU",
"https://hentaiapk.com/wp-content/uploads/2020/07/ecchi-wallpaper-1080p_3575968.png",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ741BFwxexoXRVsZe7VVI9_O8gOElAeMvXgw&usqp=CAU",
"https://images-ext-1.discordapp.net/external/L7AKoTjP2yZCqBQT1vGjeq8WFG_cPuSzS32JP3Ml4pg/https/cdn.zerotwo.dev/FUCK/137a9fbf-87bd-496c-8def-7c2d18ed4b27.gif",
"https://cdn.sex.com/images/pinporn/2018/07/24/19759095.gif?width=300",
"https://cdn.sex.com/images/pinporn/2017/03/26/17542758.gif?width=300",
]
belledp = [
"https://leaknudes.com/Uploads/Media/Jan21/Sat16/5474/m_86b50442.jpg",
"https://leaknudes.com/Uploads/Media/Jan21/Sat16/5473/m_5551b40a.jpg",
"https://leaknudes.com/Uploads/Media/Jan21/Sat16/5472/m_566e097f.jpg",
"https://leaknudes.com/Uploads/Media/Jan21/Wed13/5454/m_d4e2b0c1.jpg",
"https://leaknudes.com/Uploads/Media/Jan21/Sun10/5446/m_57e36f55.jpg",
"https://leaknudes.com/Uploads/Media/Jan21/Wed13/5453/m_b6603eb8.jpg",
"https://leaknudes.com/Uploads/Media/Jan21/Sun10/5438/m_97545b13.jpg",
"https://leaknudes.com/Uploads/Media/Jan21/Fri01/5391/m_df6128d6.jpg",
"https://influencersgonewild.com/wp-content/uploads/2020/12/belle_delphine_second_hardcore_porn_onlyfans_video_leaked-GUQIUS-364x205.jpg",
"https://mobile.twitter.com/flamemaster248/status/1338680632503840774?s=21",
]
class nsfw(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
            print("[!]nsfw cog online")

    @commands.command()
    @commands.is_nsfw()
    async def hentai(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"{random.choice(hentaidp)} ")

    @commands.command()
    @commands.is_nsfw()
    async def belle_delphine(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"{random.choice(belledp)} ")

    @commands.command()
    @commands.is_nsfw()
    async def pussy(self, ctx):
        await ctx.message.delete()
        async with request("GET", pussyurl, headers=[]) as response:
            if response.status == 200:
                data = await response.json()
                await ctx.send(data["url"])

    @commands.command()
    @commands.is_nsfw()
    async def lesbian(self, ctx):
        await ctx.message.delete()
        async with request("GET", lesurl, headers=[]) as response:
            if response.status == 200:
                data = await response.json()
                await ctx.send(data["url"])

    @commands.command()
    @commands.is_nsfw()
    async def blowjob(self, ctx):
        await ctx.message.delete()
        async with request("GET", blowjoburl, headers=[]) as response:
            if response.status == 200:
                data = await response.json()
                await ctx.send(data["url"])

    @commands.command()
    @commands.is_nsfw()
    async def boobs(self, ctx):
        await ctx.message.delete()
        async with request("GET", booburl, headers=[]) as response:
            if response.status == 200:
                data = await response.json()
                await ctx.send(data["url"])
    @commands.command()
    @commands.is_nsfw()
    async def hentai_gif(self, ctx):
        await ctx.message.delete()
        async with request("GET", hentaiurl, headers=[]) as response:
            if response.status == 200:
                data = await response.json()
                await ctx.send(data["url"])

    @commands.command()
    @commands.is_nsfw()
    async def feet(self, ctx):
        await ctx.message.delete()
        async with request("GET", feeturl, headers=[]) as response:
            if response.status == 200:
                data = await response.json()
                await ctx.send(data["url"])
                
    @commands.command()
    @commands.is_nsfw()
    async def anal(self, ctx):
        await ctx.message.delete()
        async with request("GET", analurl, headers=[]) as response:
            if response.status == 200:
                data = await response.json()
                await ctx.send(data["url"])

def setup(client):
    client.add_cog(nsfw(client))