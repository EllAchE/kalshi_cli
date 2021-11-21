import requests

from kalshi.ENVIRONMENT import API_PREFIX

# Separated to use as a proxy to determine if a token is still valid
from kalshi.auth_methods import getStoredCookie, sendRequestAndRetryOnAuthFailure


def getAllMarketsWithAuth(): # Returns detail on ALL markets in json.
    callUrl = '{}/markets'.format(API_PREFIX)
    return sendRequestAndRetryOnAuthFailure(requests.get, url=callUrl, headers={"Authorization": 'Bearer {}'.format(getStoredCookie())})
    #return requests.get(url=callUrl, headers={"Authorization": 'Bearer {}'.format(authCookie)})
