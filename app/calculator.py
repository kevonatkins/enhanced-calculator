from __future__ import annotations
from .calculator_config import load_config
from .exceptions import CalculatorError
from .input_validators import validate_two_numbers
from .operations import make_operation
from .calculation import Calculation
from .history import History
from .logger import get_logger
from .observers import LoggingObserver, AutoSaveObserver

class Calculator:
    def __init__(self):
        self.cfg = load_config()
        self.history = History(self.cfg["CALCULATOR_MAX_HISTORY_SIZE"])
        # register observers here
        # 1) logging
        self._logger = get_logger() 
        self.history.register_observer(LoggingObserver())
        # 2) auto-save
        if self.cfg["CALCULATOR_AUTO_SAVE"]:
            self.history.register_observer(
                AutoSaveObserver(
                    self.history,
                    self.cfg["CALCULATOR_HISTORY_FILE"],
                    self.cfg["CALCULATOR_DEFAULT_ENCODING"],
                )
            )

    def calculate(self, op_name: str, a, b):
        # validate inputs and enforce max range
        a, b = validate_two_numbers(a, b, self.cfg["CALCULATOR_MAX_INPUT_VALUE"])
        spec = make_operation(op_name)
        # run calculation
        c = Calculation(op_name=spec.name, a=a, b=b)
        result = c.execute()
        if isinstance(result, float):
            result = round(result, self.cfg["CALCULATOR_PRECISION"])
            c.result = result
        # record into history (this will trigger observers)
        self.history.push(c)
        return result 
    
    def save_history(self):
        self.history.save_csv(
            self.cfg["CALCULATOR_HISTORY_FILE"],
            self.cfg["CALCULATOR_DEFAULT_ENCODING"],
        )

    def load_history(self):
        self.history.load_csv(self.cfg["CALCULATOR_HISTORY_FILE"])