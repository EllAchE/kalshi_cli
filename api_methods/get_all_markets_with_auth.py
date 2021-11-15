import requests

def getAllMarketsWithAuth(authCookie): # Returns detail on ALL markets in json.
    callUrl = 'https://trading-api.kalshi.com/v1/markets'
    # return requests.get(url=callUrl, auth=authCookie)
    return requests.get(url=callUrl, headers={"Authorization": 'Bearer {}'.format(authCookie)})
