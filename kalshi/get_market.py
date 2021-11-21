import requests

# https://kalshi-public-docs.s3.amazonaws.com/KalshiAPI.html#operation/GetMarket
from kalshi.ENVIRONMENT import API_PREFIX
from kalshi.auth_methods import getValidUserIdAndCookie, getStoredCookie
from kalshi.utils import bytesToJson, sendRequestAndRetryOnAuthFailure


def printMarketOrderBook(marketId): # id is not available via UI and is not the suffix in market urls.
    url = '{}/markets/{}/order_book'.format(API_PREFIX, marketId) # this is cached so delayed
    response = requests.get(url=url, headers={"Authorization": 'Bearer {}'.format(getStoredCookie())})
    jsonResponse = bytesToJson(response.content)
    noInterest = jsonResponse['order_book']['yes']
    yesInterest = jsonResponse['order_book']['no']
    print('noInterest:\n', noInterest)
    print('yesInterest:\n', yesInterest)

def getMarketByTicker(ticker):
    url = '{}/markets_by_ticker/{}'.format(API_PREFIX, ticker)
    # response = requests.get(url=url)
    response = sendRequestAndRetryOnAuthFailure(requests.get, url=url)
    return bytesToJson(response.content)