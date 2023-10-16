import time

from util.discord import *
from util.logger import *
from util.commun import *
from util.file import *

import requests

class messages:
    @staticmethod
    def intro():
        MessageManager.intro()
        messages.view_messages(FileManager.getConfig()["token"])
        MessageManager.menu()

    @staticmethod
    def view_messages(token: str):
        logger.pending_red("Gathering messages...", "Authorizing", token)

        req = requests.get("https://discord.com/api/v9/users/@me/channels", headers=DiscordRequests.headers(token))
        channels_data = req.json()

        # Create a dictionary to store messages linked to each user
        user_messages = {}

        for channel in channels_data:
            channel_id = channel["id"]
            messages_req = requests.get(f"https://discord.com/api/v9/channels/{channel_id}/messages",
                                        headers=DiscordRequests.headers(token))
            messages_data = messages_req.json()

            # Log the messages or process them as needed
            for message in messages_data:
                # Log the message or perform any other desired actions
                logger.success_red(f"Message in channel", str(channel_id), str(message['content']))

                # Store the message content linked to each user
                author_username = message['author']['username']
                if author_username not in user_messages:
                    user_messages[author_username] = []
                user_messages[author_username].append(message["content"])

        # Combine the user messages with the channel data
        for channel in channels_data:
            recipients = channel["recipients"]
            for recipient in recipients:
                author_username = recipient["username"]
                if author_username in user_messages:
                    channel["messages"] = {author_username: user_messages[author_username]}

        FileManager.writeCache(FileManager.getConfig()["username"] + "-dm-channels", channels_data)

        logger.success_red("Gathered information", str(req.json()), token)
        time.sleep(5)

