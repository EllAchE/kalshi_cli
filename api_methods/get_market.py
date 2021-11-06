import requests

# https://kalshi-public-docs.s3.amazonaws.com/KalshiAPI.html#operation/GetMarket

def printMarketOrderBook(market_id):
    url = 'https://trading-api.kalshi.com/v1/markets/{}/order_book'.format(market_id) # this is cached so delayed
    response = requests.get(url)
    noInterest = response.raw.no
    yesInterest = response.raw.yes
    print('noInterest:\n', noInterest)
    print('yesInterest:\n', yesInterest)
