import time

from util.discord import *
from util.logger import *
from util.commun import *
from util.proxy import *
from util.file import *

import requests

class mass_dm:

    @staticmethod
    def intro():
        MessageManager.intro()

        message = logger.input("Enter the message: ")
        mass_dm.get_channels(FileManager.getConfig()["token"], message)

        # Send back to main menu when complete
        MessageManager.menu()

    @staticmethod
    def get_channels(token, message):
        global channelIds
        channelIds = requests.get("https://discord.com/api/v9/users/@me/channels",
                                  headers=DiscordRequests.headers(token)).json()
        if not channelIds:
            print(
                f'{Fore.WHITE} [{Fore.RED}ERR{Fore.WHITE}] {Fore.RED}Token has no direct messages{Fore.WHITE}')

        channels = []
        for i in range(0, len(channelIds), 3):
            channels.append(channelIds[i:i + 3])

        for channel in channels:
            t = threading.Thread(target=mass_dm.message_all, args=(token, channel, message))
            t.start()

    @staticmethod
    def message_all(token, channels, message):
        for channel in channels:
            for user in [x["username"] + "#" + x["discriminator"] for x in channel["recipients"]]:
                req = requests.post(f'https://discord.com/api/v9/channels/' + channel['id'] + '/messages',
                    headers={'Authorization': token},
                    data={"content": f"{message}"})

                if req.status_code == 200:
                    logger.success_red(f"Messaged {user}", str(req.reason), token)
                else:
                    logger.error("Failed to message", req.text)
