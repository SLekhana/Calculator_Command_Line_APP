"""Handles creation and execution of calculations."""

from dataclasses import dataclass


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
        """Return a Calculation object for given operands and operation."""
        if not callable(operation):
            raise ValueError("Invalid operation name")
        return Calculation(a, b, operation)
