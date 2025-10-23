class CalculatorError(Exception):
    """Base class for calculator errors."""

class OperationError(CalculatorError):
    """Unsupported or invalid operation."""

class ValidationError(CalculatorError):
    """Invalid user input or out-of-range value."""

class PersistenceError(CalculatorError):
    """CSV/IO related errors."""