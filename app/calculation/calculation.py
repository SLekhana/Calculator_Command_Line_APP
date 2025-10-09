"""Handles creation and execution of calculations."""

from dataclasses import dataclass
from app.operation import operations


@dataclass
class Calculation:
    """Represents a single arithmetic calculation."""
    a: float
    b: float
    operation: callable

    def perform(self):
        """Perform the calculation and return the result."""
        try:
            return self.operation(self.a, self.b)
        except ZeroDivisionError:  # pragma: no cover
            raise ZeroDivisionError("Cannot divide by zero")  # pragma: no cover

    def execute(self):
        """Alias for perform, for backward compatibility."""
        return self.perform()

    def __repr__(self):
        op_name = getattr(self.operation, "__name__", str(self.operation))
        return f"Calculation({self.a}, {self.b}, {op_name})"


class CalculationFactory:
    """Factory for creating Calculation instances."""

    @staticmethod
    def create(a: float, b: float, operation):
        """Create and return a Calculation object."""
        op_map = {
            "add": operations.add,
            "subtract": operations.subtract,
            "multiply": operations.multiply,
            "divide": operations.divide,
        }

        if isinstance(operation, str):
            operation = op_map.get(operation)

        if not callable(operation):
            raise ValueError("Invalid operation name")  # pragma: no cover

        return Calculation(a, b, operation)
