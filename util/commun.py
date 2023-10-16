from pystyle import Colors, Colorate

from util.methods import *
from util.file import *

from colorama import Fore
import datetime
import os

class ProjectInfo:
    name = "Nova"
    version = "1.0"
    discord = "discord.gg/urdesires"
    author = "Devuxious"

class MessageManager:
    @staticmethod
    def intro():
        os.system("cls")
        print(f'''{Fore.LIGHTRED_EX}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                            ███╗   ██╗ ██████╗ ██╗   ██╗ █████╗ 
                                            ████╗  ██║██╔═══██╗██║   ██║██╔══██╗
                                            ██╔██╗ ██║██║   ██║██║   ██║███████║
                                            ██║╚██╗██║██║   ██║╚██╗ ██╔╝██╔══██║
                                            ██║ ╚████║╚██████╔╝ ╚████╔╝ ██║  ██║
                                            ╚═╝  ╚═══╝ ╚═════╝   ╚═══╝  ╚═╝  ╚═╝
                                          {ProjectInfo.discord} | {ProjectInfo.version} | {ProjectInfo.author}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
''')


    @staticmethod
    def menu():
        clear()
        MessageManager.intro()
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        text = f'''
        
{Fore.LIGHTBLACK_EX}{current_time} [{Fore.RED}Token Information{Fore.LIGHTBLACK_EX}]
{Fore.LIGHTBLACK_EX}{current_time} {Fore.LIGHTBLACK_EX}- {Fore.LIGHTRED_EX}Username: {FileManager.getConfig()["username"]}
{Fore.LIGHTBLACK_EX}{current_time} {Fore.LIGHTBLACK_EX}- {Fore.LIGHTRED_EX}Token: {FileManager.getConfig()["token"]}
        
{Fore.LIGHTBLACK_EX}{current_time} [{Fore.RED}Spammer{Fore.LIGHTBLACK_EX}]
{Fore.LIGHTBLACK_EX}{current_time} [{Fore.LIGHTRED_EX}1{Fore.LIGHTBLACK_EX}] - {Fore.LIGHTRED_EX}Mass DM

{Fore.LIGHTBLACK_EX}{current_time} [{Fore.RED}Nuker{Fore.LIGHTBLACK_EX}]
{Fore.LIGHTBLACK_EX}{current_time} [{Fore.LIGHTRED_EX}3{Fore.LIGHTBLACK_EX}] - {Fore.LIGHTRED_EX}Friend Remover
{Fore.LIGHTBLACK_EX}{current_time} [{Fore.LIGHTRED_EX}4{Fore.LIGHTBLACK_EX}] - {Fore.LIGHTRED_EX}Server Leaver
{Fore.LIGHTBLACK_EX}{current_time} [{Fore.LIGHTRED_EX}5{Fore.LIGHTBLACK_EX}] - {Fore.LIGHTRED_EX}Profile Changer

{Fore.LIGHTBLACK_EX}{current_time} [{Fore.RED}Information{Fore.LIGHTBLACK_EX}]
{Fore.LIGHTBLACK_EX}{current_time} [{Fore.LIGHTRED_EX}6{Fore.LIGHTBLACK_EX}] - {Fore.LIGHTRED_EX}View Friends
{Fore.LIGHTBLACK_EX}{current_time} [{Fore.LIGHTRED_EX}7{Fore.LIGHTBLACK_EX}] - {Fore.LIGHTRED_EX}View Servers
{Fore.LIGHTBLACK_EX}{current_time} [{Fore.LIGHTRED_EX}8{Fore.LIGHTBLACK_EX}] - {Fore.LIGHTRED_EX}View Messages
{Fore.LIGHTBLACK_EX}{current_time} [{Fore.LIGHTRED_EX}9{Fore.LIGHTBLACK_EX}] - {Fore.LIGHTRED_EX}View Token Info
                '''

        print(text)

    @staticmethod
    def auth_banner():
        MessageManager.intro()
        auth = Colorate.Horizontal(Colors.blue_to_purple,  '''\n
                [1] LOGIN
                [2] REGISTER
                [3] FORGOT PASSWORD
                [4] EXIT APPLICATION
            ''')
        print(auth)
