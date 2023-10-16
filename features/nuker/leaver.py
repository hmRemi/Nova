from util.logger import *
from util.commun import *
import time

class leaver:
    @staticmethod
    def intro():
        MessageManager.intro()
        leaver.leave_servers(FileManager.getConfig()["token"])
        MessageManager.menu()

    @staticmethod
    def leave_servers(token: str):
        logger.pending_red("Leaving servers...", "Authorizing", token)
        time.sleep(2)
