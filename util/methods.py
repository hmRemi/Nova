import os

def clear():
    os.system("cls")


def getTempDir():
    system = os.name
    if system == 'nt':
        return os.getenv('temp')
    elif system == 'posix':
        return '/tmp/'
