import requests
from auth.auth_methods import getValidUserIdAndCookie
# https://kalshi-public-docs.s3.amazonaws.com/KalshiAPI.html#operation/UserGetMarketPositions
from cli.utils import bytesToJson


def getPositions(): # id is not available via UI and is not the suffix in market urls.
    userId, cookie = getValidUserIdAndCookie()
    getPositionsWithAuth(userId, cookie)

def getPositionsWithAuth(userId, cookie):
    url = 'https://trading-api.kalshi.com/v1/users/{}/positions'.format(userId)
    response = requests.get(url=url, headers={"Authorization": 'Bearer {}'.format(cookie)}) # cookie may need to be a tuple
    jsonResponse = bytesToJson(response.content)
    for market in jsonResponse['market_positions']:
        print(market['market_id'], market['position'])