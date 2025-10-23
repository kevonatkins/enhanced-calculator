from app.calculator_memento import Caretaker

def test_caretaker_undo_redo_roundtrip():
    c = Caretaker()
    state = [1, 2]
    c.save(state)           # snapshot [1,2]
    state.append(3)         # now [1,2,3]
    snap = c.undo(state)    # should go back to [1,2]
    assert snap == [1,2]

    # redo should bring us to [1,2,3]
    snap2 = c.redo([1,2])
    assert snap2 == [1,2,3]

def test_caretaker_empty_paths():
    c = Caretaker()
    assert c.undo([]) is None
    assert c.redo([]) is None