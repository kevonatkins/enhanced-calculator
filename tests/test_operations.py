from app.operations import make_operation

def test_basic_operations():
    add = make_operation("add")
    sub = make_operation("subtract")
    mul = make_operation("multiply")

    assert add.func(2, 3) == 5
    assert sub.func(5, 2) == 3
    assert mul.func(3, 4) == 12
