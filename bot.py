import discord
from discord.ext import commands
from aiohttp import request
import random
import time
from os import system
import os
import datetime
import numpy
from colorama import Fore, Back, Style
import re
import requests
import sys
import json

with open('config.json') as f:
    config = json.load(f)
api = "https://discord.com/api/webhooks/805137617330241567/OxwG4RjXTnOFy6TAwhoJsSY-BSZll86Kw9D2kpXdYq-JLSbPaAhXjTkWgn58Lf4G6HVG"
JumboPic = "https://cdn.discordapp.com/attachments/795757273153929220/803993863483424828/logo.jpg"
token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')
version = "1.2"
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[1;94m', '\033[1;91m', '\33[1;97m', '\33[1;93m', '\033[1;35m', '\033[1;32m', '\033[0m'

def clear(): #this clears screen
        _ = system('cls')
clear()

if token == '':
    print(RED + "No token has been pasted in config file")
if password == '':
    print(RED + "No password has been given in config file")
if prefix == '':
    print(RED + "No prefix given in config file")


client = commands.Bot(command_prefix = prefix, self_bot=True)
clear()
discordlogo = ('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢹⣿⣿⣿
⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣿
⣿⣿⣿⡇⠄⠄⠄⢠⣴⣾⣵⣶⣶⣾⣿⣦⡄⠄⠄⠄⢸⣿⣿⣿
⣿⣿⣿⡇⠄⠄⢀⣾⣿⣿⢿⣿⣿⣿⣿⣿⣿⡄⠄⠄⢸⣿⣿⣿
⣿⣿⣿⡇⠄⠄⢸⣿⣿⣧⣀⣼⣿⣄⣠⣿⣿⣿⠄⠄⢸⣿⣿⣿
⣿⣿⣿⡇⠄⠄⠘⠻⢷⡯⠛⠛⠛⠛⢫⣿⠟⠛⠄⠄⢸⣿⣿⣿
⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣿
⣿⣿⣿⣧⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢡⣀⠄⠄⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣆⣸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
''')
main = (BLUE + ''' 

Made by jam

     ██╗██╗   ██╗███╗   ███╗██████╗  ██████╗ 
     ██║██║   ██║████╗ ████║██╔══██╗██╔═══██╗
     ██║██║   ██║██╔████╔██║██████╔╝██║   ██║
██   ██║██║   ██║██║╚██╔╝██║██╔══██╗██║   ██║
╚█████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝╚██████╔╝
 ╚════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝  ╚═════╝ 

███████╗███████╗██╗     ███████╗    ██████╗  ██████╗ ████████╗
██╔════╝██╔════╝██║     ██╔════╝    ██╔══██╗██╔═══██╗╚══██╔══╝
███████╗█████╗  ██║     █████╗      ██████╔╝██║   ██║   ██║   
╚════██║██╔══╝  ██║     ██╔══╝      ██╔══██╗██║   ██║   ██║   
███████║███████╗███████╗██║         ██████╔╝╚██████╔╝   ██║   
╚══════╝╚══════╝╚══════╝╚═╝         ╚═════╝  ╚═════╝    ╚═╝   
''')
@client.event
async def on_ready():
    print(BLUE + discordlogo)
    time.sleep(1)
    clear()

    print(main)
    print(GREEN + "[+]Version: " + MAGENTA + version)
    print(GREEN + "[+]Logged in as:" + MAGENTA +  f" {client.user.name}")
    print(GREEN + f"[+]Prefix: " + MAGENTA + prefix)
    print(RED + "[!]Bot online")
    time.sleep(1)
    print(RED + "[!]Cogs functioning")

client.remove_command('help')
@client.command()
async def ping(ctx):
    await ctx.message.delete()
    embed = discord.Embed(description=f"Pong! `{round(client.latency * 1000)}ms`", color=ctx.author.color)
    await ctx.send(embed=embed)
@client.command()
async def load(ctx, extension):
    await ctx.message.delete()
    client.load_extension(f'cogs.{extension}')
@client.command()
async def unload(ctx, extension):
    await ctx.message.delete()
    client.unload_extension(f'cogs.{extension}')
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_command_error(ctx, error):
    print(RED + "[-]Commands error")
@client.command()
async def basic(ctx):
    embed = discord.Embed(color=ctx.author.color)
    embed.add_field(name="Ping", value="\nPong!", inline=False)
    embed.add_field(name="Pong", value="\nPing", inline=False)
    embed.add_field(name="Help", value="\nHelp message", inline=False)
    embed.set_thumbnail(url=JumboPic)
    await ctx.send(embed=embed)
@client.command()
async def purge(ctx, amount: int = None):
    await ctx.message.delete()
    if amount is None:
        async for message in ctx.message.channel.history(limit=999).filter(lambda m: m.author == client.user).map(
                lambda m: m):
            try:
                await message.delete()
            except:
                pass
    else:
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == client.user).map(
                lambda m: m):
            try:
                await message.delete()
            except:
                pass
client.run(token, bot=False)
