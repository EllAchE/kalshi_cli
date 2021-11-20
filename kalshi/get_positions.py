# https://kalshi-public-docs.s3.amazonaws.com/KalshiAPI.html#operation/UserGetMarketPositions
import requests

from kalshi.ENVIRONMENT import API_PREFIX
from kalshi.auth_methods import getValidUserIdAndCookie
from kalshi.utils import bytesToJson


def getPositions(): # id is not available via UI and is not the suffix in market urls.
    userId, cookie = getValidUserIdAndCookie()
    getPositionsWithAuth(userId, cookie)

def getPositionsWithAuth(userId, cookie):
    url = '{}/users/{}/positions'.format(API_PREFIX, userId)
    response = requests.get(url=url, headers={"Authorization": 'Bearer {}'.format(cookie)}) # cookie may need to be a tuple
    jsonResponse = bytesToJson(response.content)
    for market in jsonResponse['market_positions']:
        print(market['market_id'], market['position'])