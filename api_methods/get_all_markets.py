import requests

# https://kalshi-public-docs.s3.amazonaws.com/KalshiAPI.html#operation/GetMarkets
from api_methods.auth import getValidUserIdAndCookie


def getAllMarkets(): # Returns detail on ALL markets in json.
    user_id, cookie = getValidUserIdAndCookie()
    return getAllMarketsWithAuth(cookie)

def getAllMarketsWithAuth(cookie): # Returns detail on ALL markets in json.
    url = 'https://trading-api.kalshi.com/v1/markets'
    return requests.get(url=url, auth=cookie)
