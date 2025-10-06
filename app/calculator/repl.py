"""REPL (Read-Eval-Print Loop) for the command-line calculator."""

from app.operation import operations
from app.calculation.calculation import CalculationFactory


def repl():
    """Run the calculator REPL interface."""
    print("Calculator REPL. Type 'help' for commands.")

    history = []
    valid_ops = {
        "add": operations.add,
        "subtract": operations.subtract,
        "multiply": operations.multiply,
        "divide": operations.divide,
    }

    while True:
        try:
            user_input = input(">>> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            raise SystemExit

        if user_input == "exit":
            print("Goodbye!")
            raise SystemExit

        elif user_input == "help":
            print(
                "Available commands:\n"
                "  add, subtract, multiply, divide <num1> <num2>\n"
                "  history   - Show calculation history\n"
                "  help      - Show this help message\n"
                "  exit      - Exit the calculator"
            )
            continue

        elif user_input == "history":
            if not history:
                print("No calculations yet.")
            else:
                print("Calculation History:")
                for item in history:
                    print(item)
            continue

        elif not user_input:
            continue

        # Parse input
        parts = user_input.split()
        if len(parts) != 3:
            print("Invalid command. Try again or type 'help'.")
            continue

        operation, num1, num2 = parts
        if operation not in valid_ops:
            print("Invalid command. Type 'help' for a list of commands.")
            continue

        try:
            a, b = float(num1), float(num2)
        except ValueError:
            print("Invalid numbers. Please enter numeric values.")
            continue

        try:
            # Create calculation via factory (string-based)
            calc = CalculationFactory.create(a, b, operation)

            # Execute the calculation
            if hasattr(calc, "perform"):
                result = calc.perform()
            elif callable(calc):
                result = calc()
            else:
                raise TypeError("Invalid calculation object")

            print(f"Result: {result}")
            history.append(f"{operation}({a}, {b}) = {result}")

        except ZeroDivisionError:
            print("Error: Division by zero")
        except TypeError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")
