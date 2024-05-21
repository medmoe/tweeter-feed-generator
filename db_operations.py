import logging

import psycopg2

from constants import db_name, user, password, host, port

logger = logging.getLogger()


def connect_to_db():
    try:
        connection = psycopg2.connect(database=db_name, user=user, password=password, host=host, port=port)
        logger.info("Connected to Database OK.")
    except Exception as e:
        logger.error("Connecting to Database error: %s", e)
        raise e
    return connection


def insert_record(cur, id, text, date):
    try:
        datetime_formatted = date.strftime('%Y-%m-%d %H:%M:%S')
        query = "INSERT INTO tweet (id, text, date) VALUES (%s, %s, %s)"
        cur.execute(query, (id, text, datetime_formatted))
        logger.info("Record saved OK")
    except Exception as e:
        logger.error("Saving record error: %s", e)
        raise e
