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
        return self.operation(self.a, self.b)


class CalculationFactory:
    """Factory class to create Calculation objects."""

    @staticmethod
    def create(a: float, b: float, operation):
        """
        Return a Calculation object for given operands and operation.

        Accepts operation as either:
        - a callable (e.g., operations.add), or
        - a string ('add', 'subtract', 'multiply', 'divide').
        """
        op_map = {
            "add": operations.add,
            "subtract": operations.subtract,
            "multiply": operations.multiply,
            "divide": operations.divide,
        }

        # Convert string operation to function if needed
        if isinstance(operation, str):
            if operation not in op_map:
                raise ValueError("Invalid operation name")
            operation = op_map[operation]

        if not callable(operation):
            raise ValueError("Invalid operation name")

        return Calculation(a, b, operation)
