import requests

# https://kalshi-public-docs.s3.amazonaws.com/KalshiAPI.html#operation/Login

def login(email, password):
    url = 'https://trading-api.kalshi.com/v1/log_in'
    requestBody = {
        "email": email,
        "password": password
    }
    response = requests.post(url=url, data=requestBody)
    # containers user_id, token (cookie?) and access_level