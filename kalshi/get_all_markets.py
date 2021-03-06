# https://kalshi-public-docs.s3.amazonaws.com/KalshiAPI.html#operation/GetMarkets
import json
import os

import requests

from kalshi.ENVIRONMENT import API_PREFIX
from kalshi.auth_methods import sendRequestAndRetryOnAuthFailure, getStoredCookie
from kalshi.utils import bytesToJson


def getAllMarkets(): # Returns detail on ALL markets in json.
    marketsResponse = getAllMarketsWithAuth()
    jsonMarketResponse = bytesToJson(marketsResponse.content)
    print(os.getcwd())
    with open('data/markets.json', 'w') as jsonMarketFile:
        json.dump(jsonMarketResponse, jsonMarketFile)
    print('saved updated markets locally')
    return jsonMarketResponse

def getAllMarketsCached(): # Returns detail on ALL markets in json. Should not require auth, but should be delayed due to caching
    callUrl = '{}/cached/markets/'.format(API_PREFIX)
    return sendRequestAndRetryOnAuthFailure(requests.get, url=callUrl)
    # return requests.get(url=callUrl)

def getAllMarketsWithAuth(): # Returns detail on ALL markets in json.
    callUrl = '{}/markets'.format(API_PREFIX)
    return sendRequestAndRetryOnAuthFailure(requests.get, url=callUrl, headers={"Authorization": 'Bearer {}'.format(getStoredCookie())})
    #return requests.get(url=callUrl, headers={"Authorization": 'Bearer {}'.format(authCookie)})

