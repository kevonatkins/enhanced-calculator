import pytest
from app.calculator import Calculator
from app.exceptions import ValidationError, OperationError

def test_validation_and_unknown_op(tmp_path, monkeypatch):
    monkeypatch.setenv("CALCULATOR_LOG_DIR", str(tmp_path / "log"))
    monkeypatch.setenv("CALCULATOR_HISTORY_DIR", str(tmp_path / "hist"))

    calc = Calculator()
    # unknown op
    with pytest.raises(OperationError):
        calc.calculate("not_an_op", 1, 2)
    # validator max range
    monkeypatch.setenv("CALCULATOR_MAX_INPUT_VALUE", "1")
    calc2 = Calculator()
    with pytest.raises(ValidationError):
        calc2.calculate("add", 10, 0)