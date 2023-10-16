import time

from util.discord import *
from util.logger import *
from util.commun import *
from util.file import *

import requests

class guild_info:
    @staticmethod
    def intro():
        MessageManager.intro()
        guild_info.view_info(FileManager.getConfig()["token"])
        MessageManager.menu()

    @staticmethod
    def view_info(token: str):
        logger.pending_red("Gathering information...", "Authorizing", token)

        req = requests.get("https://discord.com/api/v10/users/@me/guilds", headers=DiscordRequests.headers(token))

        FileManager.writeCache(FileManager.getConfig()["username"] + "-guilds", req.json())

        logger.success_red("Gathered information", str(req.json()), token)
        time.sleep(5)

