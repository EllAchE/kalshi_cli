# https://kalshi-public-docs.s3.amazonaws.com/KalshiAPI.html#operation/GetMarkets
from api_methods.get_all_markets_with_auth import getAllMarketsWithAuth
from auth.auth_methods import getValidUserIdAndCookie

def getAllMarkets(): # Returns detail on ALL markets in json.
    user_id, cookie = getValidUserIdAndCookie()
    return getAllMarketsWithAuth(cookie)
