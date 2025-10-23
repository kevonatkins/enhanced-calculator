from app.history import History
from app.calculation import Calculation

def test_history_push_undo_redo_and_clear():
    h = History(max_size=10)
    c1 = Calculation("add", 1, 2); c1.execute()
    c2 = Calculation("multiply", 2, 3); c2.execute()

    h.push(c1); h.push(c2)
    assert [c.op_name for c in h.list()] == ["add", "multiply"]

    h.undo()
    assert [c.op_name for c in h.list()] == ["add"]

    h.redo()
    assert [c.op_name for c in h.list()] == ["add", "multiply"]

    h.clear()
    assert h.list() == []

def test_history_csv_roundtrip(tmp_path):
    h = History(max_size=10)
    c1 = Calculation("add", 5, 7); c1.execute()
    c2 = Calculation("divide", 8, 4); c2.execute()
    h.push(c1); h.push(c2)

    f = tmp_path / "hist.csv"
    h.save_csv(str(f))
    assert f.exists()

    # load into a new History instance
    h2 = History(max_size=10)
    h2.load_csv(str(f))
    ops = [c.op_name for c in h2.list()]
    assert ops == ["add", "divide"]
    results = [c.result for c in h2.list()]
    assert results == [12, 2]