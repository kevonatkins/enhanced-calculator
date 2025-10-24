import logging
from logging.handlers import RotatingFileHandler
from .calculator_config import load_config

def get_logger(log_file: str| None = None):
    if log_file is None:
        cfg = load_config()
        log_file = cfg["CALCULATOR_LOG_FILE"]
        
    logger = logging.getLogger("calc")
    if logger.handlers:  # reuse handler in tests
        return logger
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(log_file, maxBytes=200_000, backupCount=2)
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.addHandler(handler)
    return logger