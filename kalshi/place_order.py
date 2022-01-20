import requests

# https://kalshi-public-docs.s3.amazonaws.com/KalshiAPI.html#operation/UserOrderCreate
# side must be 'yes' or 'no'
# expiration in seconds I believe, todo - accept days, hours minutes etc. in expiration
from kalshi.ENVIRONMENT import API_PREFIX
from kalshi.auth_methods import getStoredUserId, getStoredCookie, sendRequestAndRetryOnAuthFailure


# def placeMarketOrder(amount, marketId, price, side, expiration=None, maxCost=None, sellPositionCapped=None):
#     userId, cookie = getValidUserIdAndCookie()
#     placeOrderWithAuth(userId, cookie, amount, marketId, price, side, expiration, maxCost, sellPositionCapped)
from kalshi.ticker_to_id import getIdFromTicker
from kalshi.utils import bytesToJson

def placeMarketOrderTicker(amount, ticker, side, expiration=0): # todo check if 0 seconds is supported
    return placeOrderTicker(amount, ticker, 0.99, side, expiration)

def placeOrderTicker(amount, ticker, price, side, expiration=None, maxCost=None, sellPositionCapped=None):
    marketId = getIdFromTicker(ticker)
    return placeOrder(amount, marketId, price, side, expiration, maxCost, sellPositionCapped)

def placeOrder(amount, marketId, price, side, expiration=None, maxCost=None, sellPositionCapped=None):
    url = '{}/users/{}/orders'.format(API_PREFIX, getStoredUserId())
    requestBody = {
        "count": amount,
        "market_id": marketId,
        "price": price,
        "side": side
    }
    if expiration != None:
        requestBody['expiration_unix_ts'] = expiration
    if maxCost != None:
        requestBody['max_cost_cents'] = maxCost
    if sellPositionCapped != None:
        requestBody['sell_position_capped'] = sellPositionCapped

    response = sendRequestAndRetryOnAuthFailure(requests.post, url=url, headers={"Authorization": 'Bearer {}'.format(getStoredCookie())}, data=requestBody)
    jsonResponse = bytesToJson(response.content)
    if response.status_code == 200:
        print('placed order!')
    return jsonResponse
    #return requests.post() # will want to print result