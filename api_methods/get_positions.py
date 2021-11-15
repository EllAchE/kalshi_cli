import requests

# https://kalshi-public-docs.s3.amazonaws.com/KalshiAPI.html#operation/UserGetMarketPositions

def getPositions():
    url = 'https://trading-api.kalshi.com/v1/users/{}/positions'.format(userId)
    response = requests.get(url=url, auth=cookie) # cookie may need to be a tuple
    return response.market_positions