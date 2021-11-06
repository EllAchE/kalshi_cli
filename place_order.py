import requests

# https://kalshi-public-docs.s3.amazonaws.com/KalshiAPI.html#operation/UserOrderCreate

def placeOrder(userId, cookie, count, marketId, price, side, expiration=None, maxCost=None, sellPositionCapped=None):
    url = 'https://trading-api.kalshi.com/v1/users/{}/orders'.format(userId)
    requestBody = {
        "count": count,
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

    requests.post(url, auth=cookie, data=requestBody)