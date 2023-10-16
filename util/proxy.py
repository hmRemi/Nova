import requests, os, sys, re, time, random, os.path, string, subprocess, random, threading, ctypes, shutil
from time import sleep

from util.methods import *
from util.logger import *
from util.file import *

class Proxy:
    @staticmethod
    def proxy():
        proxies = open(FileManager.proxiesFile).read().split('\n')
        proxy = proxies[0]

        with open(FileManager.proxiesFile, 'r+') as fp:
            lines = fp.readlines()
            fp.seek(0)
            fp.truncate()
            fp.writelines(lines[1:])
        return {'http://': f'http://{proxy}', 'https://': f'https://{proxy}'}
