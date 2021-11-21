import requests

# https://kalshi-public-docs.s3.amazonaws.com/KalshiAPI.html#operation/UserOrderCreate
# side must be 'yes' or 'no'
# expiration in seconds I believe, todo - accept days, hours minutes etc. in expiration
from kalshi.ENVIRONMENT import API_PREFIX
from kalshi.auth_methods import getValidUserIdAndCookie, getStoredUserId, getStoredCookie, \
    sendRequestAndRetryOnAuthFailure


# def placeMarketOrder(amount, marketId, price, side, expiration=None, maxCost=None, sellPositionCapped=None):
#     userId, cookie = getValidUserIdAndCookie()
#     placeOrderWithAuth(userId, cookie, amount, marketId, price, side, expiration, maxCost, sellPositionCapped)

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

    return sendRequestAndRetryOnAuthFailure(requests.post, auth=getStoredCookie(), data=requestBody)
    #return requests.post(url, auth=getStoredCookie(), data=requestBody) # will want to print result