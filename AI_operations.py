import logging
import time

import google.generativeai as genai

from constants import gemini_key

logger = logging.getLogger()


def get_tweet(prompt):
    tweet = generate_tweet(prompt)
    while len(tweet) > 280:
        logger.warning("The tweet is too long. Trying again ...")
        time.sleep(5)
        tweet = generate_tweet(prompt)
    return tweet


def generate_tweet(prompt: str):
    genai.configure(api_key=gemini_key)
    model = genai.GenerativeModel('gemini-pro')
    try:
        response = model.generate_content(prompt)
        logger.info("Tweet generated OK")
    except Exception as e:
        logger.error("Generating tweet error: %s", e)
        raise e
    return response.text
