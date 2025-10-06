from app.operation import operations

class Calculation:
    """Represents a single calculation."""

    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def execute(self):
        """Execute the stored operation."""
        return self.operation(self.a, self.b)


class CalculationFactory:
    """Factory to create Calculation objects."""

    @staticmethod
    def create(a, b, operation_name):
        operations_map = {
            "add": operations.add,
            "subtract": operations.subtract,
            "multiply": operations.multiply,
            "divide": operations.divide,
        }

        if operation_name not in operations_map:
            raise ValueError("Invalid operation name")

        return Calculation(a, b, operations_map[operation_name])

