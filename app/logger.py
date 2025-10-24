import logging
from pathlib import Path  
from logging.handlers import RotatingFileHandler
from .calculator_config import load_config

def get_logger(log_file: str| None = None):
    if log_file is None:
        cfg = load_config()
        log_file = cfg["CALCULATOR_LOG_FILE"]
    desired = str(Path(log_file))
    
    #make sure directoru exists 
    Path(log_file).parent.mkdir(parents=True, exist_ok=True)
        
    logger = logging.getLogger("calc")


     # If a handler exists but points to a different file (e.g., from a previous test),
    # remove old handlers so we can attach a new one to 'desired'.
    needs_reset = True
    for h in list(logger.handlers):
        base = getattr(h, "baseFilename", None)
        if base and str(base) == desired:
            needs_reset = False
        else:
            logger.removeHandler(h)

    if needs_reset:
        logger.setLevel(logging.INFO)
        handler = RotatingFileHandler(desired, maxBytes=200_000, backupCount=2)
        handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
        logger.addHandler(handler)

    return logger