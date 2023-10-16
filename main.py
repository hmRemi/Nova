from features.info.token_info import *
from features.info.messages import *
from features.info.friends import *
from features.info.guild import *
from features.nuker.leaver import *

from features.spammer.massdm import *
from util.auth import *

from util.discord import *
from util.methods import *
from util.commun import *
from util.logger import *
from util.proxy import *
from util.file import *

from colorama import Fore
import requests
import socket
import time

def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest

keyauthapp = api(
    name="Nova",
    ownerid="0o7kucftP7",
    secret="f7ef16a4664bee5ada781224cc9aa1954eec3e34429e2a72eba0ca1f2a8de1ae",
    version="1.0",
    hash_to_check=getchecksum()
)
class authorization():
    @staticmethod
    def login():
        clear()
        MessageManager.intro()

        username = logger.input("Enter username: ")
        password = logger.input("Enter password: ")

        logger.pending_red("Logging in...", "Authorizing", username)

        keyauthapp.login(username, password)
        token_login.enter_token()


class token_login():
    @staticmethod
    def enter_token():
        clear()
        MessageManager.intro()

        if FileManager.getConfig()["token"] != "":
            input = logger.input("Found token in config.json, would you like to use it? (y/n): ")

            if input.lower() == "y":
                token_login.check_token(FileManager.getConfig()["token"])
            else:
                entered_token = logger.input("Enter token: ")
                token_login.check_token(entered_token)
        else:
            entered_token = logger.input("Enter token: ")
            token_login.check_token(entered_token)

    def check_token(token: str):
        logger.pending_red("Logging in...", "Authorizing", token)

        req = requests.get("https://discord.com/api/v9/users/@me", headers=DiscordRequests.headers(token))

        if req.status_code == 200:
            username = str(req.json()["username"])
            logger.success_red("Logged into " + username, str(req.reason), token)

            # Save token to config.json
            config = FileManager.getConfig()
            config["token"] = token
            config["username"] = username
            FileManager.writeConfig(config)

            time.sleep(2)
            main_menu.main()
        else:
            logger.error("Invalid token", str(req.reason))
            time.sleep(2)
            token_login.enter_token()


class main_menu():
    @staticmethod
    def main():
        MessageManager.menu()
        while True:
            option = input(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTRED_EX}{socket.gethostname()}{Fore.LIGHTBLACK_EX}]{Fore.WHITE} > ")

            if option == "1":
                mass_dm.intro()
            elif option == "4":
                leaver.intro()
            elif option == "6":
                friends.intro()
            elif option == "7":
                guild_info.intro()
            elif option == "8":
                messages.intro()
            elif option == "9":
                token_info.intro()
            else:
                print(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTRED_EX}ERROR{Fore.LIGHTBLACK_EX}] {Fore.WHITE}Option does not exist")

if __name__ == '__main__':
    FileManager.validateConfigurationFile()
    authorization.login()
