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

    

def _print_help():  # pragma: no cover
    print("Commands:")
    print("  add|subtract|multiply|divide|power|root|modulus|int_divide|percent|abs_diff a b")
    print("  history | clear | undo | redo")
    print("  save | load")
    print("  help | exit")

def repl():  # pragma: no cover
    from colorama import Fore, Style, init as color_init
    color_init(autoreset=True)
    calc = Calculator()
    print(Fore.CYAN + "Enhanced Calculator. Type 'help' for commands.")
    while True:
        try:
            raw = input(Style.BRIGHT + "> ").strip()
            if not raw:
                continue
            parts = raw.split()
            cmd, args = parts[0].lower(), parts[1:]

            if cmd in {"help"}:
                _print_help(); continue
            if cmd == "exit":
                print(Fore.YELLOW + "Bye!"); return
            if cmd == "history":
                for c in calc.history.list():
                    print(f"{c.ts} | {c.op_name}({c.a}, {c.b}) = {c.result}")
                continue
            if cmd == "clear":
                calc.history.clear(); print(Fore.YELLOW + "History cleared."); continue
            if cmd == "undo":
                calc.history.undo(); print(Fore.YELLOW + "Undo done."); continue
            if cmd == "redo":
                calc.history.redo(); print(Fore.YELLOW + "Redo done."); continue
            if cmd == "save":
                calc.save_history(); print(Fore.GREEN + "History saved."); continue
            if cmd == "load":
                calc.load_history(); print(Fore.GREEN + "History loaded."); continue

            # assume operation with two args
            if cmd:
                if len(args) != 2:
                    print(Fore.RED + "Need exactly two numbers.")
                    continue
                res = calc.calculate(cmd, args[0], args[1])
                print(Fore.GREEN + f"= {res}")
            else:
                print(Fore.RED + "Unknown command. Type 'help'.")
        except CalculatorError as ce:
            print(Fore.RED + f"Error: {ce}")
        except SystemExit:
            print(Fore.YELLOW + "Bye!"); return
        except Exception as e:
            print(Fore.RED + f"Unexpected error: {e}")

if __name__ == "__main__":  # pragma: no cover
    repl()