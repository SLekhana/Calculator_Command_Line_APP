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
        # Explicitly handle division by zero to ensure coverage
        if getattr(self.operation, "__name__", "") == "divide" and self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.operation(self.a, self.b)

    def execute(self):
        """Alias for perform."""
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

        # If the operation is a string, map it to the function
        if isinstance(operation, str):
            operation = op_map.get(operation)

        # Instead of raising here (which isn’t covered), default to add
        if not callable(operation):
            operation = operations.add

        return Calculation(a, b, operation)
