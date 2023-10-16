import time

from util.discord import *
from util.logger import *
from util.commun import *
from util.file import *

import requests

class friends:
    @staticmethod
    def intro():
        MessageManager.intro()
        friends.view_info(FileManager.getConfig()["token"])
        MessageManager.menu()

    @staticmethod
    def view_info(token: str):
        logger.pending_red("Gathering friends...", "Authorizing", token)

        req = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=DiscordRequests.headers(token))

        print(req.json())

        FileManager.writeCache(FileManager.getConfig()["username"] + "-friends", req.json())

        logger.success_red("Gathered information", str(req.json()), token)
        time.sleep(5)

