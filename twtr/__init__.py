import os
import tweepy
from dotenv import load_dotenv

def tweet(text):
    load_dotenv()  # Load env vars when function is called, not at import time
    bearer_token = os.getenv('TWEEPY_BEARER_TOKEN')
    consumer_key = os.getenv('TWEEPY_CONSUMER_KEY')
    consumer_secret = os.getenv('TWEEPY_CONSUMER_SECRET')
    access_token = os.getenv('TWEEPY_ACCESS_TOKEN')
    access_token_secret = os.getenv('TWEEPY_ACCESS_TOKEN_SECRET')
    if not all([bearer_token, consumer_key, consumer_secret, access_token, access_token_secret]):
        raise RuntimeError('Missing Twitter API keys. See the [README](https://pypi.org/project/twtr/) for setup instructions.')
    client = tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )
    try:
        client.create_tweet(text=text)
    except tweepy.errors.Unauthorized:
        raise RuntimeError('401 Unauthorized: Check the [README](https://pypi.org/project/twtr/) to set up your Twitter API keys.')
