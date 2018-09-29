import requests
from api import db


def get_content():
    headers = db.headers
    response = requests.get(db.api_url, headers=headers)
    json_response = response.json()[0]
    tweet = json_response['quote'] + '-' + json_response['autor']

    return tweet
