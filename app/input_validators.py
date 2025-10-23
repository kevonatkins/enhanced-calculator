from .exceptions import ValidationError

def _to_number(x):
    try:
        return float(x)
    except Exception as exc:  
        raise ValidationError(f"Not a number: {x}") from exc

def validate_two_numbers(a, b, max_abs):
    a = _to_number(a)
    b = _to_number(b)
    for v in (a, b):
        if abs(v) > max_abs:
            raise ValidationError(f"Input {v} exceeds max allowed {max_abs}")
    return a, b