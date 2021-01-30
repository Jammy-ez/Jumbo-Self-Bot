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
JumboPic = "https://cdn.discordapp.com/attachments/795757273153929220/803993863483424828/logo.jpg"
token = ""
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[1;94m', '\033[1;91m', '\33[1;97m', '\33[1;93m', '\033[1;35m', '\033[1;32m', '\033[0m'
client = commands.Bot(command_prefix = '.', self_bot=True)
def clear(): #this clears screen
        _ = system('cls')
clear()
if token == '':
    token = input(MAGENTA + "Enter discord token: ")
version = "1.0"
main = (MAGENTA + ''' 
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
    print(main)
    print("Version --> " + version)
    print(f"Logged in as --> {client.user.name}")
    print("[!]Bot online")

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
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"[ERROR] Command not found!", delete_after=3)
    elif isinstance(error, commands.CheckFailure):
        await ctx.send('[ERROR]: You\'re missing permission to execute this command', delete_after=3)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"[ERROR]: Missing arguments: {error}", delete_after=3)
    elif isinstance(error, numpy.AxisError):
        await ctx.send('Invalid Image', delete_after=3)
    elif isinstance(error, discord.errors.Forbidden):
        await ctx.send(f"[ERROR]: 404 Forbidden Access: {error}", delete_after=3)
    elif "Cannot send an empty message" in error_str:
        await ctx.send('[ERROR]: Message contents cannot be null', delete_after=3)
    else:
        ctx.send(f'[ERROR]: unable to find error')
@client.command()
async def basic(ctx):
    embed = discord.Embed(color=ctx.author.color)
    embed.add_field(name="Ping", value="\nPong!", inline=False)
    embed.add_field(name="Pong", value="\nPing", inline=False)
    embed.add_field(name="Help", value="\nHelp message", inline=False)
    embed.set_thumbnail(url=JumboPic)
    await ctx.send(embed=embed)
client.run(token, bot=False)