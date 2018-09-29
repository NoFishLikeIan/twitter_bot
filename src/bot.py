import tweepy
from content import get_content
from api import db

auth = tweepy.OAuthHandler(db.twitter_api, db.twitter_api_secret)
auth.set_access_token(db.twitter_access_token, db.twitter_access_token_secret)

api = tweepy.API(auth)

api.update_status(
    'Hello world! This is the first tweet from your bot, it is indeed a test')
