from datetime import datetime
from colorama import init, Fore
import threading

lock = threading.RLock()

class logger:
    def success(text1, text2=None):
        date = datetime.now()
        time = datetime.strftime(date, "%H:%M:%S")
        lock.acquire()
        if text2 != None:
            print(
                Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTBLUE_EX + time + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTBLUE_EX + "*" + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTBLUE_EX + text1 + Fore.LIGHTBLACK_EX + " | " + Fore.LIGHTBLUE_EX + text2)
        else:
            print(
                Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTBLUE_EX + time + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTBLUE_EX + "*" + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTBLUE_EX + text1)
        lock.release()

    def debug(text1, text2=None):
        date = datetime.now()
        time = datetime.strftime(date, "%H:%M:%S")
        lock.acquire()
        if text2 != None:
            print(
                Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTYELLOW_EX + time + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTYELLOW_EX + "^" + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTYELLOW_EX + text1 + Fore.LIGHTBLACK_EX + " | " + Fore.LIGHTYELLOW_EX + text2)
        else:
            print(
                Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTYELLOW_EX + time + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTYELLOW_EX + "^" + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTYELLOW_EX + text1)

        lock.release()

    def pending(text1, text2=None):
        date = datetime.now()
        time = datetime.strftime(date, "%H:%M:%S")
        lock.acquire()
        if text2 != None:
            print(
                Fore.LIGHTBLACK_EX + "[ " + Fore.YELLOW + time + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTBLACK_EX + "[ " + Fore.YELLOW + "^" + Fore.LIGHTBLACK_EX + " ] " + Fore.YELLOW + text1 + Fore.LIGHTBLACK_EX + " | " + Fore.YELLOW + text2)
        else:
            print(
                Fore.LIGHTBLACK_EX + "[ " + Fore.YELLOW + time + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTBLACK_EX + "[ " + Fore.YELLOW + "^" + Fore.LIGHTBLACK_EX + " ] " + Fore.YELLOW + text1)

        lock.release()

    def pending_red(text1, text2, text3):
        date = datetime.now()
        time = datetime.strftime(date, "%H:%M:%S")
        lock.acquire()
        print(
            Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTRED_EX + time + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTRED_EX + "/" + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTRED_EX + text1 + Fore.LIGHTBLACK_EX + " | " + Fore.LIGHTRED_EX + text2 + Fore.LIGHTBLACK_EX + " | " + Fore.LIGHTRED_EX + text3)
        lock.release()

    def generated(text1, text2):
        date = datetime.now()
        time = datetime.strftime(date, "%H:%M:%S")
        lock.acquire()
        print(
            Fore.LIGHTBLACK_EX + "[ " + Fore.CYAN + time + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTBLACK_EX + "[ " + Fore.CYAN + "#" + Fore.LIGHTBLACK_EX + " ] " + Fore.CYAN + text1 + Fore.LIGHTBLACK_EX + " | " + Fore.CYAN + text2)
        lock.release()

    def success_green(text1, text2, text3):
        date = datetime.now()
        time = datetime.strftime(date, "%H:%M:%S")
        lock.acquire()
        print(
            Fore.LIGHTBLACK_EX + "[ " + Fore.GREEN + time + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTBLACK_EX + "[ " + Fore.GREEN + "*" + Fore.LIGHTBLACK_EX + " ] " + Fore.GREEN + text1 + Fore.LIGHTBLACK_EX + " | " + Fore.GREEN + text2 + Fore.LIGHTBLACK_EX + " | " + Fore.GREEN + text3)
        lock.release()

    def success_red(text1, text2, text3):
        date = datetime.now()
        time = datetime.strftime(date, "%H:%M:%S")
        lock.acquire()
        print(
            Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTRED_EX + time + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTRED_EX + "*" + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTRED_EX + text1 + Fore.LIGHTBLACK_EX + " | " + Fore.LIGHTRED_EX + text2 + Fore.LIGHTBLACK_EX + " | " + Fore.LIGHTRED_EX + text3)
        lock.release()

    def error_2(text1, text2, text3):
        date = datetime.now()
        time = datetime.strftime(date, "%H:%M:%S")
        lock.acquire()
        print(
            Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTRED_EX + time + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTRED_EX + "ERROR" + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTRED_EX + text1 + Fore.LIGHTBLACK_EX + " | " + Fore.LIGHTRED_EX + text2 + Fore.LIGHTBLACK_EX + " | " + Fore.LIGHTRED_EX + text3)
        lock.release()

    def error(text1, text2):
        date = datetime.now()
        time = datetime.strftime(date, "%H:%M:%S")
        lock.acquire()
        print(
            Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTRED_EX + time + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTRED_EX + "!" + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTRED_EX + text1 + Fore.LIGHTBLACK_EX + " | " + Fore.LIGHTRED_EX + text2)
        lock.release()

    def error_3(text1, text2, text3):
        date = datetime.now()
        time = datetime.strftime(date, "%H:%M:%S")
        lock.acquire()
        print(
            Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTRED_EX + time + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTRED_EX + "!" + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTRED_EX + text1 + Fore.LIGHTBLACK_EX + " | " + Fore.LIGHTRED_EX + text2 + Fore.LIGHTBLACK_EX + " | " + Fore.LIGHTRED_EX + text3)
        lock.release()

    def input(text):
        date = datetime.now()
        time = datetime.strftime(date, "%H:%M:%S")
        print(
            Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTRED_EX + time + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTBLACK_EX + "[ " + Fore.LIGHTRED_EX + ">" + Fore.LIGHTBLACK_EX + " ] " + Fore.LIGHTRED_EX + text,
            end="")
        return input(Fore.WHITE + "")