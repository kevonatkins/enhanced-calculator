import pytest
from app.operations import make_operation

def test_basic_operations():
    add = make_operation("add")
    sub = make_operation("subtract")
    mul = make_operation("multiply")

    assert add.func(2, 3) == 5
    assert sub.func(5, 2) == 3
    assert mul.func(3, 4) == 12

def test_divide_and_zero():
    div = make_operation("divide")
    assert div.func(8, 4) == 2
    with pytest.raises(Exception):
        div.func(1, 0)


def test_power_and_int_divide():
    pow_op = make_operation("power")
    idiv = make_operation("int_divide")

    assert pow_op.func(2, 3) == 8
    assert pow_op.func(9, 0.5) == 3  # square root via power just as a quick sanity

    assert idiv.func(7, 3) == 2
    assert idiv.func(-7, 3) == -2   # trunc toward 

def test_modulus_and_abs_diff():
    mod = make_operation("modulus")
    absd = make_operation("abs_diff")

    assert mod.func(10, 3) == 1
    assert absd.func(-2, 4) == 6

    with pytest.raises(Exception):
        mod.func(5, 0)

def test_root_and_percent():
    rt = make_operation("root")
    pct = make_operation("percent")

    # 27^(1/3) = 3
    assert pytest.approx(rt.func(27, 3), rel=1e-6) == 3

    # odd root of negative is allowed: (-8)^(1/3) = -2
    assert pytest.approx(rt.func(-8, 3), rel=1e-6) == -2

    # even root of negative is invalid
    with pytest.raises(Exception):
        rt.func(-16, 2)

    # 0th root undefined
    with pytest.raises(Exception):
        rt.func(9, 0)

    # percent: (50 / 200) * 100 = 25.0
    assert pct.func(50, 200) == 25.0

    # denominator zero invalid
    with pytest.raises(Exception):
        pct.func(1, 0)