import discord, subprocess, sys, time, os, colorama, ctypes, json, requests, random, pytz
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from datetime import datetime
from threading import Thread
from sys import argv
from colorama import Fore
from discord.ext import commands

def clear():
    os.system('cls')
    os.system("mode con cols=59 lines=20")

def startup():
    print(f'{Fore.RED}d')
clear()

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))


token = ('token here')
purgemessage = ('purge word here')


class MyClient(discord.Client):
    async def on_message(self, message):
        if(message.author!=self.user):
            return
        channels=[]
        if(message.content=="purge_server"):
            channels=message.channel.guild.channels
        elif(message.content==purgemessage):
            channels.append(message.channel)
        else:
            return
        for channel in channels:
            print(f'{Fore.RED}Purging In:{Fore.CYAN} {channel}')
            try:
                async for mss in channel.history(limit=None):

                    if(mss.author==self.user):
                        print(f'{Fore.CYAN}Message {Fore.CYAN}Deleted {Fore.RED}-> {Fore.CYAN}{mss.content}')
                        try:
                            await mss.delete()
                        except:
                            print("Couldn't delete!")
            except:
                print("Can't read history!\n")

def start():
    print(f'''
{Fore.RED} ┌─┐┬ ┬┬─┐┌─┐┌─┐┬─┐
{Fore.CYAN} ├─┘│ │├┬┘│ ┬├┤ ├┬┘
{Fore.WHITE} ┴  └─┘┴└─└─┘└─┘┴└ 

 Send {Fore.RED}[{Fore.RED}{purgemessage}{Fore.RED}] {Fore.WHITE}To Delete Msgs
''')
os.system(f'title Message Purger')
clear()
start()

bot=MyClient(heartbeat_timeout=86400, guild_subscriptions=False)
bot.run(token, bot=False)
