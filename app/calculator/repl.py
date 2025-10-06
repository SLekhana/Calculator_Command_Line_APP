"""
Simple REPL that uses CalculationFactory from app.calculation.
The __main__ guard is excluded from coverage.
"""

from app.calculation import CalculationFactory

def print_help():
    """Display help information for the user."""
    print("Available commands:")
    print("  help     - Show this help message")
    print("  history  - Show calculation history")
    print("  exit     - Exit the calculator")
    print("Usage:")
    print("  <operation> <num1> <num2>")
    print("Operations: add, subtract, multiply, divide")

def repl():
    """Run the Read-Eval-Print Loop for the calculator."""
    history = []
    print("Calculator REPL. Type 'help' for commands.")

    while True:
        try:
            raw = input("calc> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            raise SystemExit  # pragma: no cover

        if not raw:
            continue

        if raw.lower() == "exit":
            print("Goodbye!")
            raise SystemExit

        elif raw.lower() == "help":
            print_help()
            continue

        elif raw.lower() == "history":
            if not history:
                print("No calculations yet.")
            else:
                for calc in history:
                    print(calc)
            continue

        parts = raw.split()
        if len(parts) != 3:
            print("Invalid command format. Try 'help' for usage.")
            continue

        operation, num1, num2 = parts
        try:
            num1, num2 = float(num1), float(num2)
        except ValueError:
            print("Invalid numbers. Try again.")
            continue

        try:
            calc = CalculationFactory.create_calculation(operation, num1, num2)
            result = calc.perform()
            print(f"Result: {result}")
            history.append(f"{operation}({num1}, {num2}) = {result}")
        except ZeroDivisionError:
            print("Error: Division by zero.")
        except Exception:
            print("Invalid command. Try again or type 'help'.")

if __name__ == "__main__":  # pragma: no cover
    repl()

# Alias for testing
main = repl

