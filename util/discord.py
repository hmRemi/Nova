import requests

class DiscordRequests:

    xsp = 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjAuMS45Iiwib3NfdmVyc2lvbiI6IjEwLjAuMTc3NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTM1NTQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'

    @staticmethod
    def finger():
        r = requests.get('https://discordapp.com/api/v9/experiments')
        if r.status_code == 200:
            fingerprint = r.json()['fingerprint']
            return fingerprint
        else:
            print('Error fetched fingerprint')

    @staticmethod
    def headers(token: str):
        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-GB',
            'authorization': token,
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/channels/@me',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'cookie': '__dcfduid=23a63d20476c11ec9811c1e6024b99d9; __sdcfduid=23a63d21476c11ec9811c1e6024b99d9e7175a1ac31a8c5e4152455c5056eff033528243e185c5a85202515edb6d57b0; locale=en-GB',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.1.9 Chrome/83.0.4103.122 Electron/9.4.4 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-context-properties': 'eyJsb2NhdGlvbiI6IlVzZXIgUHJvZmlsZSJ9',
            'x-fingerprint': DiscordRequests.finger(),
            'x-super-properties': DiscordRequests.xsp,
            'te': 'trailers',
        }

        return headers