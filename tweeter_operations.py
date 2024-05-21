import logging

import tweepy

from constants import bearer, consumer_key, consumer_secret, access_token, access_token_secret

logger = logging.getLogger()


def authenticate():
    try:
        client = tweepy.Client(bearer_token=bearer,
                               consumer_key=consumer_key,
                               consumer_secret=consumer_secret,
                               access_token=access_token,
                               access_token_secret=access_token_secret)
        logger.info("Authentication OK.")
    except Exception as e:
        logger.error("Authentication error: %s", e)
        raise e
    return client


def post_tweet(client, tweet):
    try:
        response = client.create_tweet(text=tweet)
        logger.info("Tweet posted OK.")
    except Exception as e:
        logger.error("Posting tweet error: %s", e)
        raise e
    return response
