import re
import os
import discord
import asyncio
import requests
import time
from time import sleep
from tqdm import tqdm
from colorama import Fore as C
from discord.ext import commands

def anti_afk():
    os.system('cls')

    bot = commands.Bot(command_prefix="!")

    token =  ('enter token here')
    r = ('enter what you want to respond to afk checks with')
    d = ('enter the delay you would like to use')


    @bot.event
    async def on_ready():
        os.system(f'title [Anti-AFK]')
        os.system(f'mode 60,20')
        os.system('cls')
        print(f'''
    {C.WHITE}        ┌─┐┌┐┌┌┬┐┬  ┌─┐┌─┐┬┌─  ┌─┐┬ ┬┌─┐┌─┐┬┌─
    {C.RED}        ├─┤│││ │ │  ├─┤├┤ ├┴┐  │  ├─┤├┤ │  ├┴┐
    {C.WHITE}        ┴ ┴┘└┘ ┴ ┴  ┴ ┴└  ┴ ┴  └─┘┴ ┴└─┘└─┘┴ ┴
    {C.RED}          ┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
    {C.WHITE}                    Login:{C.RED}[{C.WHITE}{bot.user.name}{C.RED}#{C.WHITE}{bot.user.discriminator}{C.RED}]
    {C.WHITE}                    Response:{C.RED}[{C.WHITE}{r}{C.RED}]
    {C.WHITE}                    Delay:{C.RED}[{C.WHITE}{d}{C.RED}]{C.WHITE} Seconds
    {C.RED}          ┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙
    ''')


    @bot.event
    async def on_message(x):
        if f"<@!{bot.user.id}>" in x.content.lower() or 'afk' in x.content.lower() and '1' in x.content.lower():
            await asyncio.sleep(int(d))
            await x.channel.send(r)
            print(f'{C.RED}<{C.WHITE}+{C.RED}> {C.WHITE}1{C.RED} AFK Check Blocked -> {C.WHITE}{x.author} {C.RED}')

    bot.run(token, bot=False)






class Main():
    def __init__(self) -> None:
        self._banner = """
           
                    ██╗██╗  ██╗███████╗██████╗
                    ██║██║  ██║██╔════╝██╔══██╗
                    ██║███████║█████╗  ██████╔╝
                    ██║██╔══██║██╔══╝  ██╔══██╗
                    ██║██║  ██║███████╗██████╔╝
                    ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝       
                ╔══════════════════════════════════════════════╗
                ║                                              ║
                ║    [1] ANTI-AFK      [3] AUTO-PRESSER        ║
                ║    [2] AFK CHECKER   [4] BLOCK-BYPASS        ║
                ║                                              ║
                ╚══════════════════════════════════════════════╝               
        """
    def _home(self):
        os.system('title PRIVATE STAMINA [MULTI-TOOL]')
        print(self._banner)
        _v       = int(("1"))
        _choices = [1, 2, 3, 4]
        
        if _v in _choices:
            if _v == 3:
                auto_presser()
            
            if _v == 1:
                anti_afk()
            
            if _v == 2:
                afk_checker()

            if _v == 4:
                anti_block()

        if _v not in _choices:
                print("Invalid option")
                time.sleep(1)
                Main()._home()


if __name__ == '__main__':
    Main()._home()
