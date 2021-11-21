import json

from kalshi.get_all_markets import getAllMarkets


def printHelpCommands():
    print(getHelpMessage())

def getHelpMessage():
    return "usage: kalshi [option] [parameters]\nOptions are 'buy', 'sell', 'getMarket', 'getAllMarkets' 'positions'\n"

def bytesToJson(bytes):
    strValue = bytes.decode()
    return json.loads(strValue)

def generateExpirationSeconds(seconds=0, minutes=0, hours=0, days=0):
    return seconds + 60 * minutes + 3600 * hours + 24 * 3600 * days

