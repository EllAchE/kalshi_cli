# https://kalshi-public-docs.s3.amazonaws.com/KalshiAPI.html#operation/GetMarkets
import json

from api_methods.get_all_markets_with_auth import getAllMarketsWithAuth
from auth.auth_methods import getValidUserIdAndCookie
from cli.utils import bytesToJson


def getAllMarkets(): # Returns detail on ALL markets in json.
    user_id, cookie = getValidUserIdAndCookie()
    marketsResponse = getAllMarketsWithAuth(cookie)
    jsonMarketResponse = bytesToJson(marketsResponse.content)
    with open('../data/markets.json') as jsonMarketFile:
        json.dump(jsonMarketFile)
    print('saved updated markets locally')
    return jsonMarketResponse
