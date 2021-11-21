import json

from kalshi import logger
from kalshi.auth_methods import regenerateCredentials


def printHelpCommands():
    print(getHelpMessage())

def getHelpMessage():
    return "usage: kalshi [option] [parameters]\nOptions are 'buy', 'sell', 'getMarket', 'getAllMarkets' 'positions'\n"

def bytesToJson(bytes):
    strValue = bytes.decode()
    return json.loads(strValue)

def generateExpirationSeconds(seconds=0, minutes=0, hours=0, days=0):
    return seconds + 60 * minutes + 3600 * hours + 24 * 3600 * days

def sendRequestAndRetryOnAuthFailure(retrievalFunction, **kwargs):
    try:
        response = retrievalFunction(**kwargs)
        if response.status_code != 200: # todo validate that response codes for bad auth can only be in [401, 403] then look for these rather than non 200
            regenerateCredentials()
            return retrievalFunction(**kwargs)
        else:
            return response
    except Exception as e:
        logger.error(e)