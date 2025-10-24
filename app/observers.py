from __future__ import annotations
from .logger import get_logger

class Observer:
    """Observer base class."""
    def update(self, calc_dict: dict) -> None:
        raise NotImplementedError

class LoggingObserver(Observer):
    """Logs each calculation: op, operands, result, timestamp."""
    def __init__(self):
        self.logger = get_logger()

    def update(self, calc_dict: dict) -> None:
        # Example: {"operation":"add","a":2,"b":3,"result":5,"timestamp":"..."}
        self.logger.info("calc %s", calc_dict)

class AutoSaveObserver(Observer):
    """Auto-saves full history to CSV whenever a calculation is added."""
    def __init__(self, history, file_path: str, encoding: str = "utf-8"):
        self.history = history
        self.file_path = file_path
        self.encoding = encoding

    def update(self, _calc_dict: dict) -> None:
        self.history.save_csv(self.file_path, self.encoding)