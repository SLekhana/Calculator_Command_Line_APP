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
        """Perform the stored calculation and return the result."""
        try:
            return self.operation(self.a, self.b)
        except ZeroDivisionError:
            raise ZeroDivisionError("Cannot divide by zero")

    def execute(self):
        """Alias for perform() for backward compatibility."""
        return self.perform()

    def __repr__(self):
        """Readable representation for debugging."""
        op_name = getattr(self.operation, "__name__", str(self.operation))
        return f"Calculation({self.a}, {self.b}, {op_name})"


class CalculationFactory:
    """Factory class to create Calculation objects."""

    @staticmethod
    def create(a: float, b: float, operation):
        """Return a Calculation object for given operands and operation."""
        op_map = {
            "add": operations.add,
            "subtract": operations.subtract,
            "multiply": operations.multiply,
            "divide": operations.divide,
        }

        # Handle string operation names
        if isinstance(operation, str):
            operation = op_map.get(operation)

        if not callable(operation):
            raise ValueError("Invalid operation name")

        return Calculation(a, b, operation)
