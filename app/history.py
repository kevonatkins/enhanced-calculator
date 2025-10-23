from pathlib import Path
import pandas as pd
from .calculation import Calculation
from .calculator_memento import Caretaker
from .exceptions import PersistenceError

class History:
    def __init__(self, max_size=1000):
        self._items: list[Calculation] = []
        self._max = max_size
        self._caretaker = Caretaker()

    def push(self, calc: Calculation):
        if len(self._items) >= self._max:
            self._items.pop(0)
        self._caretaker.save(self._items)
        self._items.append(calc)

    def list(self):
        return list(self._items)

    def clear(self):
        self._caretaker.save(self._items)
        self._items.clear()

    def undo(self):
        snap = self._caretaker.undo(self._items)
        if snap is not None:
            self._items = snap

    def redo(self):
        snap = self._caretaker.redo(self._items)
        if snap is not None:
            self._items = snap

    # serialization (CSV)
    def to_dataframe(self):
        return pd.DataFrame([c.to_dict() for c in self._items])

    def save_csv(self, file_path: str, encoding="utf-8"):
        try:
            df = self.to_dataframe()
            Path(file_path).parent.mkdir(parents=True, exist_ok=True)
            df.to_csv(file_path, index=False, encoding=encoding)
        except Exception as exc:  # pragma: no cover (rare)
            raise PersistenceError(str(exc)) from exc

    def load_csv(self, file_path: str):
        try:
            df = pd.read_csv(file_path)
        except FileNotFoundError:
            return
        except Exception as exc:  # pragma: no cover
            raise PersistenceError(str(exc)) from exc
        self._items = []
        for _, row in df.iterrows():
            c = Calculation(
                op_name=row["operation"],
                a=float(row["a"]),
                b=float(row["b"]),
                result=float(row["result"]),
                ts=row["timestamp"],
            )
            self._items.append(c)