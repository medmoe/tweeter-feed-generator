import datetime
import logging
import time

from AI_operations import get_tweet
from constants import prompts
from db_operations import connect_to_db, insert_record
from settings import setup_logging
from tweeter_operations import authenticate, post_tweet


def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info(f'Application up and running.')
    client = authenticate()
    connection = connect_to_db()
    cur = connection.cursor()
    prompt_idx = 6
    try:
        while True:
            prompt = prompts[prompt_idx % len(prompts)] + " Give a concise answer that does not exceed 280 characters."
            tweet = get_tweet(prompt)
            response = post_tweet(client, tweet)
            insert_record(cur, response.data['id'], response.data['text'], datetime.datetime.now())
            connection.commit()
            time.sleep(60 * 60 * 4)
            prompt_idx += 1
    except Exception as e:
        logger.error("Ops! something went wrong: %s", e)
    finally:
        cur.close()
        connection.close()
        logger.info(f'Application stopped.')


if __name__ == "__main__":
    main()
