import json

import requests

# https://kalshi-public-docs.s3.amazonaws.com/KalshiAPI.html#operation/Login
# returns {
#   "access_level": "string",
#   "token": "string",
#   "user_id": "string"
# }

def login():
    secretsFile = open('../secrets.json')
    secretsJson = json.load(secretsFile)
    url = 'https://trading-api.kalshi.com/v1/log_in'
    requestBody = {
        "email": secretsJson.email,
        "password": secretsJson.password
    }
    return requests.post(url=url, data=requestBody)
    # containers user_id, token (cookie?) and access_leveln

def loadCredentials():
    credentialsFile = open('../credentials.json')
    return json.load(credentialsFile)

def regenerateCredentials():
    response = login()
    saveObj = {
        "cookie": response.cookie,
        "user_id": response.user_id
    }
    with open('../credentials.json', 'w') as credFile:
        json.dump(saveObj, credFile)
    print('updated credentials')
