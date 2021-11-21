import json
import requests

# https://kalshi-public-docs.s3.amazonaws.com/KalshiAPI.html#operation/Login
# returns {
#   "access_level": "string",
#   "token": "string",
#   "user_id": "string"
# }
from kalshi.logger import LOG
from kalshi.ENVIRONMENT import API_PREFIX
from kalshi.utils import bytesToJson


def login():
    with open('../secrets.json') as secretsFile:
        secretsJson = json.load(secretsFile)
    url = '{}/log_in'.format(API_PREFIX)
    requestBody = {
        "email": secretsJson['email'],
        "password": secretsJson['password']
    }
    byteResponse = requests.post(url=url, json=requestBody).content
    return bytesToJson(byteResponse)
    # containers user_id, token (cookie?) and access_leveln

def loadCredentials():
    with open('../credentials.json') as credentialsFile:
        return json.load(credentialsFile)

def regenerateCredentials():
    response = login()
    saveObj = {
        "cookie": response['token'],
        "user_id": response['user_id'],
        "access_level": response['access_level']
    }
    with open('../credentials.json', 'w') as credFile:
        json.dump(saveObj, credFile)
    print('updated credentials')

def getValidUserIdAndCookie(): # todo rather than use this hacky method, add try/catch for 200s on methods that require auth
    creds = loadCredentials()
    if creds['cookie'] is not None:
        # testMarketsCall = getAllMarketsWithAuth(creds['cookie']) # todo hacky way to see if auth is valid
        # if testMarketsCall.status_code == 200:
        return creds['user_id'], creds['cookie']

    regenerateCredentials()
    creds = loadCredentials()
    return creds['user_id'], creds['cookie']

def getStoredUserId():
    creds = loadCredentials()
    return creds['user_id']

def getStoredCookie():
    creds = loadCredentials()
    return creds['cookie']

def sendRequestAndRetryOnAuthFailure(retrievalFunction, **kwargs):
    try:
        response = retrievalFunction(**kwargs)
        if response.status_code != 200: # todo validate that response codes for bad auth can only be in [401, 403] then look for these rather than non 200
            regenerateCredentials()
            return retrievalFunction(**kwargs)
        else:
            return response
    except Exception as e:
        LOG.error(e)
