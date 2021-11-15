import requests

# https://kalshi-public-docs.s3.amazonaws.com/KalshiAPI.html#operation/GetMarkets

def getAllMarkets(): # Returns detail on ALL markets in json.
    url = 'https://trading-api.kalshi.com/v1/markets'
    return requests.get(url)
