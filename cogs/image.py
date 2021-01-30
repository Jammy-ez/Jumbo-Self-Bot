import discord
import random
from discord.ext import commands
import requests
import urllib
from aiohttp import request
#varibles
noodledp = [
"https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/simple-sesame-noodles-1597268176.jpg?crop=0.501xw:1.00xh;0.152xw,0&resize=640:*",
"https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Mama_instant_noodle_block.jpg/1200px-Mama_instant_noodle_block.jpg",
"https://images-na.ssl-images-amazon.com/images/I/81ZT7QLwReL._AC_SL1500_.jpg",
"https://assets.sainsburys-groceries.co.uk/gol/7847218/1/640x640.jpg",
"https://www.ocado.com/productImages/438/438224011_0_640x640.jpg?identifier=a7702a42f025e96ce46af132737e6c02",
"https://dmrqkbkq8el9i.cloudfront.net/Pictures/480xany/0/2/7/210027_lostthepotnoodles_463226_crop.jpg",
"https://images-na.ssl-images-amazon.com/images/I/513bHX6qLEL._AC_.jpg",
"https://digitalcontent.api.tesco.com/v2/media/ghs/4b4fea3a-9a72-4fb5-af9c-1cb061fc0465/snapshotimagehandler_1295088048.jpeg?h=540&w=540",
]
jamdp = [
"https://digitalcontent.api.tesco.com/v2/media/ghs/3e872da7-3a17-43b4-931e-e39c943004e2/snapshotimagehandler_426894617.jpeg?h=540&w=540",
"https://i.dailymail.co.uk/i/pix/2016/03/10/09/320E7D2C00000578-0-image-a-15_1457601988661.jpg",
"https://tipbuzz.com/wp-content/uploads/Jammie-Dodgers-1.jpg",
"https://veganfoodandliving-1321f.kxcdn.com/wp-content/uploads/2020/06/vegan-Jammie-Dodgers.jpg",
]
oreodp = [
"https://images.heb.com/is/image/HEBGrocery/002197320",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3ysxF6DUeEcEp6dMt1Y6cKHZRtTTLPC9v_g&usqp=CAU",
"https://cms.qz.com/wp-content/uploads/2016/10/oreos-e1476385008753.jpg?quality=75&strip=all&w=1200&h=630&crop=1"
"https://www.coop.ch/img/produkte/1200_630/RGB/4094888_001.jpg?_=1539125524913",
]
WINK = "https://some-random-api.ml/animu/wink"
HUG = "https://some-random-api.ml/animu/hug"
MEME = "https://some-random-api.ml/meme"
CAT_IMG = "https://some-random-api.ml/img/cat"
DOG_IMG = "https://some-random-api.ml/img/dog"
class image(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
            print("[!]image cog online")
    
    @commands.command()
    async def oreo_img(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"{random.choice(oreodp)} ")

    @commands.command()
    async def jam_img(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"{random.choice(jamdp)} ")

    @commands.command()
    async def noodle_img(self, ctx):
        await ctx.send(f"{random.choice(noodledp)} ")

    @commands.command()
    async def cat_img(self, ctx):
        await ctx.message.delete()
        async with request("GET", CAT_IMG, headers=[]) as response:
            if response.status == 200:
                data = await response.json()
                await ctx.send(data["link"])

    @commands.command()
    async def dog_img(self, ctx):
        await ctx.message.delete()
        async with request("GET", DOG_IMG, headers=[]) as response:
            if response.status == 200:
                data = await response.json()
                await ctx.send(data["link"])

    @commands.command()
    async def meme(self, ctx):
        await ctx.message.delete()
        async with request("GET", MEME, headers=[]) as response:
            if response.status == 200:
                data = await response.json()
                await ctx.send(data["image"])

    @commands.command()
    async def wink(self, ctx):
        await ctx.message.delete()
        async with request("GET", WINK, headers=[]) as response:
            if response.status == 200:
                data = await response.json()
                await ctx.send(data["link"])

    @commands.command()
    async def hug(self, ctx):
        await ctx.message.delete()
        async with request("GET", HUG, headers=[]) as response:
            if response.status == 200:
                data = await response.json()
                await ctx.send(data["link"])
    


def setup(client):
    client.add_cog(image(client))