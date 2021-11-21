# https://kalshi-public-docs.s3.amazonaws.com/KalshiAPI.html#operation/UserGetMarketPositions
import requests

from kalshi.ENVIRONMENT import API_PREFIX
from kalshi.auth_methods import getStoredCookie, getStoredUserId, sendRequestAndRetryOnAuthFailure
from kalshi.utils import bytesToJson


def getPositions():
    url = '{}/users/{}/positions'.format(API_PREFIX, getStoredUserId())
    # response = requests.get(url=url, headers={"Authorization": 'Bearer {}'.format(cookie)}) # cookie may need to be a tuple
    response = sendRequestAndRetryOnAuthFailure(requests.get, url=url, headers={"Authorization": 'Bearer {}'.format(getStoredCookie())})
    jsonResponse = bytesToJson(response.content)
    for market in jsonResponse['market_positions']:
        print(market['market_id'], market['position'])