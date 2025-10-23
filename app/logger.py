import logging
from logging.handlers import RotatingFileHandler

def get_logger(log_file: str):
    logger = logging.getLogger("calc")
    if logger.handlers:  # reuse handler in tests
        return logger
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(log_file, maxBytes=200_000, backupCount=2)
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.addHandler(handler)
    return logger