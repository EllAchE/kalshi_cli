import requests

# https://kalshi-public-docs.s3.amazonaws.com/KalshiAPI.html#operation/GetMarket
from kalshi.ENVIRONMENT import API_PREFIX
from kalshi.auth_methods import getValidUserIdAndCookie
from kalshi.utils import bytesToJson


def printMarketOrderBook(marketId): # id is not available via UI and is not the suffix in market urls.
    userId, cookie = getValidUserIdAndCookie()
    printMarketOrderBookWithAuth(marketId, cookie)

def printMarketOrderBookWithAuth(marketId, cookie): # id is not available via UI and is not the suffix in market urls.
    url = '{}/markets/{}/order_book'.format(API_PREFIX, marketId) # this is cached so delayed
    response = requests.get(url=url, headers={"Authorization": 'Bearer {}'.format(cookie)})
    jsonResponse = bytesToJson(response.content)
    noInterest = jsonResponse['order_book']['yes']
    yesInterest = jsonResponse['order_book']['no']
    print('noInterest:\n', noInterest)
    print('yesInterest:\n', yesInterest)

def getMarketByTicker(ticker):
