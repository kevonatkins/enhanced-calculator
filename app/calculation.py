from dataclasses import dataclass
from datetime import datetime, timezone
from .operations import make_operation

@dataclass
class Calculation:
    op_name: str
    a: float
    b: float
    result: float | None = None
    ts: str | None = None  # ISO timestamp

    def execute(self):
        spec = make_operation(self.op_name)
        self.result = spec.func(self.a, self.b)
        self.ts = datetime.now(timezone.utc).isoformat()
        return self.result

    def to_dict(self):
        return {
            "timestamp": self.ts,
            "operation": self.op_name,
            "a": self.a,
            "b": self.b,
            "result": self.result,
        }
