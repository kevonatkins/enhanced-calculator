from dataclasses import dataclass

@dataclass(frozen=True)
class Memento:
    history_snapshot: tuple

class Caretaker:
    def __init__(self):
        self._undo = []
        self._redo = []

    def save(self, history_list):
        # Save current snapshot into undo stack; clear redo
        self._undo.append(Memento(tuple(history_list)))
        self._redo.clear()

    def undo(self, history_list):
        if not self._undo:
            return None
        # push current to redo, pop last undo to restore
        self._redo.append(Memento(tuple(history_list)))
        m = self._undo.pop()
        return list(m.history_snapshot)

    def redo(self, history_list):
        if not self._redo:
            return None
        # push current to undo, pop last redo to restore
        self._undo.append(Memento(tuple(history_list)))
        m = self._redo.pop()
        return list(m.history_snapshot)