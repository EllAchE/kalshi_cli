import requests

# https://kalshi-public-docs.s3.amazonaws.com/KalshiAPI.html#operation/UserOrderCreate
# side must be 'yes' or 'no'
# expiration in seconds I believe, todo - accept days, hours minutes etc. in expiration
from kalshi.auth_methods import getValidUserIdAndCookie


def placeLimitOrder(amount, marketId, side, expiration=None, maxCost=None, sellPositionCapped=None):
    userId, cookie = getValidUserIdAndCookie()
    placeOrderWithAuth(userId, cookie, amount, marketId, 0.99, side, expiration, maxCost, sellPositionCapped) # todo add a warning when a user places a market order (or just don't enable it at all)

# def placeMarketOrder(amount, marketId, price, side, expiration=None, maxCost=None, sellPositionCapped=None):
#     userId, cookie = getValidUserIdAndCookie()
#     placeOrderWithAuth(userId, cookie, amount, marketId, price, side, expiration, maxCost, sellPositionCapped)

def placeOrderWithAuth(userId, cookie, amount, marketId, price, side, expiration=None, maxCost=None, sellPositionCapped=None):
    url = 'https://trading-api.kalshi.com/v1/users/{}/orders'.format(userId)
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

    return requests.post(url, auth=cookie, data=requestBody) # will want to print result