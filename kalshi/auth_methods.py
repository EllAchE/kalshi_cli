import json
import requests

# https://kalshi-public-docs.s3.amazonaws.com/KalshiAPI.html#operation/Login
# returns {
#   "access_level": "string",
#   "token": "string",
#   "user_id": "string"
# }
from get_all_markets_with_auth import getAllMarketsWithAuth
from utils import bytesToJson


def login():
    secretsFile = open('../secrets.json')
    secretsJson = json.load(secretsFile)
    url = 'https://trading-api.kalshi.com/v1/log_in'
    requestBody = {
        "email": secretsJson['email'],
        "password": secretsJson['password']
    }
    byteResponse = requests.post(url=url, json=requestBody).content
    return bytesToJson(byteResponse)
    # containers user_id, token (cookie?) and access_leveln

def loadCredentials():
    credentialsFile = open('../credentials.json')
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

def getValidUserIdAndCookie():
    creds = loadCredentials()
    if creds['cookie'] is not None:
        testMarketsCall = getAllMarketsWithAuth(creds['cookie']) # todo hacky way to see if auth is valid
        if testMarketsCall.status_code == 200:
            return creds['user_id'], creds['cookie']

    regenerateCredentials()
    creds = loadCredentials()
    return creds['user_id'], creds['cookie']
