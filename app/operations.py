# app/operations.py

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



# === simple factory ===

_operations = {
    "add": Operation("add", add, "Add two numbers (a + b)"),
    "subtract": Operation("subtract", subtract, "Subtract second number from first (a - b)"),
    "multiply": Operation("multiply", multiply, "Multiply two numbers (a * b)"),
    "divide": Operation("divide", divide, "Divide first by second (a / b)"),
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
