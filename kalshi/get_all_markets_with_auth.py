import requests

from kalshi.ENVIRONMENT import API_PREFIX


def getAllMarketsWithAuth(authCookie): # Returns detail on ALL markets in json.
    callUrl = '{}/markets'.format(API_PREFIX)
    return requests.get(url=callUrl, headers={"Authorization": 'Bearer {}'.format(authCookie)})
