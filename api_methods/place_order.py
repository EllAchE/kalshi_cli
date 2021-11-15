import requests

# https://kalshi-public-docs.s3.amazonaws.com/KalshiAPI.html#operation/UserOrderCreate
# side must be 'yes' or 'no'
# expiration in seconds I believe, todo - accept days, hours minutes etc. in expiration

def placeOrder(amount, marketId, price, side, expiration=None, maxCost=None, sellPositionCapped=None):
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

    requests.post(url, auth=cookie, data=requestBody)