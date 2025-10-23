# app/operations.py
import math 
from dataclasses import dataclass
from .exceptions import OperationError, ValidationError

@dataclass(frozen=True)
class Operation:
    """Represents an arithmetic operation with its function and help text."""
    name: str
    func: callable
    help: str


# === basic operations first ===

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        from .exceptions import ValidationError
        raise ValidationError("Division by zero")
    return a / b 

def power(a, b):
    return a ** b

def int_divide(a, b):
    if b == 0:
        from .exceptions import ValidationError
        raise ValidationError("Division by zero")
    # integer quotient (truncate toward 0)
    import math
    return math.trunc(a / b)

def modulus(a, b):
    if b == 0:
        from .exceptions import ValidationError
        raise ValidationError("Modulus by zero")
    return a % b

def abs_diff(a, b):
    return abs(a - b) 

def root(a, b):
    # b-th root of a
    if b == 0:
        from .exceptions import ValidationError
        raise ValidationError("0th root undefined")
    # even root of negative is invalid for real numbers
    if a < 0 and int(b) % 2 == 0:
        from .exceptions import ValidationError
        raise ValidationError("Even root of negative number")
    # support odd roots of negatives: keep sign of a
    return math.copysign(abs(a) ** (1.0 / b), 1 if a >= 0 else -1)

def percent(a, b):
    # (a / b) * 100
    if b == 0:
        from .exceptions import ValidationError
        raise ValidationError("Percent with denominator zero")
    return (a / b) * 100.0

# === simple factory ===

_operations = {
    "add": Operation("add", add, "Add two numbers (a + b)"),
    "subtract": Operation("subtract", subtract, "Subtract second number from first (a - b)"),
    "multiply": Operation("multiply", multiply, "Multiply two numbers (a * b)"),
    "divide": Operation("divide", divide, "Divide first by second (a / b)"),
    "power": Operation("power", power, "Raise a to the power b (a ** b)"),
    "int_divide": Operation("int_divide", int_divide, "Integer quotient trunc(a / b)"),
    "modulus": Operation("modulus", modulus, "Remainder of a / b (a % b)"),
    "abs_diff": Operation("abs_diff", abs_diff, "Absolute difference |a - b|"),
    "root": Operation("root", root, "b-th root of a"),
    "percent": Operation("percent", percent, "(a / b) * 100"),
}


def make_operation(name: str) -> Operation:
    """Factory that returns the operation object based on name."""
    try:
        return _operations[name.lower()]
    except KeyError as e:
        raise OperationError(f"Unsupported operation: {name}") from e


def all_operations():
    """Return list of all supported operations."""
    return list(_operations.values()) 


