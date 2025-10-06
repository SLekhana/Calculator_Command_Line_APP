"""REPL (Read-Eval-Print Loop) for the command-line calculator."""

from app.operation.operations import add, subtract, multiply, divide
from app.calculation.calculation import CalculationFactory


def repl():
    """Run the calculator REPL interface."""
    print("Calculator REPL. Type 'help' for commands.")

    history = []
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    while True:
        try:
            user_input = input(">>> ").strip().lower()
        except (EOFError, KeyboardInterrupt):  # pragma: no cover
            print("\nGoodbye!")
            break

        if user_input == "exit":
            print("Goodbye!")
            raise SystemExit

        elif user_input == "help":
            print(
                "Commands:\n"
                "  add, subtract, multiply, divide <num1> <num2>\n"
                "  history   - Show calculation history\n"
                "  help      - Show this help message\n"
                "  exit      - Exit the calculator"
            )

        elif user_input == "history":
            if not history:
                print("No calculations yet.")
            else:
                print("Calculation History:")
                for h in history:
                    print(h)

        elif user_input:
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid command. Try again or type 'help'.")
                continue

            operation, num1, num2 = parts
            if operation not in operations:
                print("Invalid operation. Type 'help' for a list of commands.")
                continue

            try:
                a, b = float(num1), float(num2)
            except ValueError:
                print("Invalid numbers. Please enter numeric values.")
                continue

            try:
                func = operations[operation]
                result = func(a, b)
                print(f"Result: {result}")
                history.append(f"{operation}({a}, {b}) = {result}")
            except ZeroDivisionError:
                print("Error: Division by zero")
            except Exception as e:  # pragma: no cover (safety net)
                print(f"Error: {e}")

        else:  # pragma: no cover
            print("Invalid input. Type 'help' for commands.")
