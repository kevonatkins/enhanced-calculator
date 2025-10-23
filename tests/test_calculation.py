from app.calculation import Calculation

def test_calculation_exec_stamps_time_and_result():
    c = Calculation("add", 2, 3)
    r = c.execute()
    assert r == 5
    assert c.result == 5
    assert isinstance(c.ts, str) and len(c.ts) > 0