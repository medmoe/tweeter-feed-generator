import os
from datetime import datetime
from logging import config


def get_log_file_path():
    current_time = datetime.now()
    log_dir = os.path.join('logs', str(current_time.year), str(current_time.month))
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f'{current_time.day}.log')
    return log_file


LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': '%(asctime)-12s %(levelname)-8s %(name)-12s %(message)s',
        },
    },
    'handlers': {
        'file': {
            'filename': get_log_file_path(),
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
}


def setup_logging():
    config.dictConfig(LOGGING_CONFIG)
