from os import mkdir, path
from util.logger import *

import json
import os

class FileManager:
    configFile = "config.json"
    proxiesFile = "proxies.txt"
    cacheFolder = "/cache/"

    defaultConfig = '''
{
    "token": "",
    "username": ""
}'''

    @staticmethod
    def validateConfigurationFile():
        if not path.exists(FileManager.configFile):
            print("Creating configuration file")
            with open(FileManager.configFile, 'w') as w:
                w.write(FileManager.defaultConfig)

        if not path.exists(FileManager.proxiesFile):
            print("Creating proxies file")
            with open(FileManager.proxiesFile, 'w') as w:
                w.write("")

    @staticmethod
    def getConfig():
        with open(FileManager.configFile) as config_file:
            config = json.load(config_file)

        return config

    @staticmethod
    def writeConfig(config):
        with open(FileManager.configFile, 'w') as config_file:
            json.dump(config, config_file, indent=4)

    @staticmethod
    def writeCache(fileName, config):
        # Get the directory of the script that calls this function (main.py in this case)
        calling_script_dir = os.path.dirname(os.path.abspath(__file__))

        # Go up one directory to reach the parent directory of main.py
        parent_dir = os.path.dirname(calling_script_dir)

        # Construct the path to the cache folder
        file_path = os.path.join(parent_dir, "cache", fileName + ".json")

        with open(file_path, 'w') as config_file:
            json.dump(config, config_file, indent=4)

            # Log a message after writing the data
            logger.error("Logged info to", file_path)
