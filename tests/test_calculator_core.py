from app.calculator import Calculator

def test_calculate_add_and_history(tmp_path, monkeypatch):
    # point config to temp dirs
    monkeypatch.setenv("CALCULATOR_LOG_DIR", str(tmp_path / "log"))
    monkeypatch.setenv("CALCULATOR_HISTORY_DIR", str(tmp_path / "hist"))
    monkeypatch.setenv("CALCULATOR_DEFAULT_ENCODING", "utf-8")
    monkeypatch.setenv("CALCULATOR_AUTO_SAVE", "true")

    calc = Calculator()
    r = calc.calculate("add", 5, 7)
    assert r == 12
    assert len(calc.history.list()) == 1

def test_calculate_precision(tmp_path, monkeypatch):
    monkeypatch.setenv("CALCULATOR_LOG_DIR", str(tmp_path / "log"))
    monkeypatch.setenv("CALCULATOR_HISTORY_DIR", str(tmp_path / "hist"))
    monkeypatch.setenv("CALCULATOR_PRECISION", "2")

    calc = Calculator()
    r = calc.calculate("divide", 1, 3)  
    assert r == 0.33  # rounded to 2 dp