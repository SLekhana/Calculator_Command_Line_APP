from app.calculation.calculation import CalculationFactory
from app.operation import operations


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

        if raw.lower() == "help":
            print(
                "Available commands:\n"
                "  help     - Show this help message\n"
                "  history  - Show calculation history\n"
                "  exit     - Exit the calculator\n"
                "Usage:\n"
                "  <operation> <num1> <num2>\n"
                "Operations: add, subtract, multiply, divide"
            )
            continue

        if raw.lower() == "history":
            if not history:
                print("No calculations yet.")
            else:
                print("History:")
                for item in history:
                    print(item)
            continue

        # Parse math operations: "<op> <num1> <num2>"
        parts = raw.split()
        if len(parts) != 3:
            print("Invalid command. Try again or type 'help'.")
            continue

        op, a_str, b_str = parts

        # Validate operation
        if op not in {"add", "subtract", "multiply", "divide"}:
            print("Invalid command. Try again or type 'help'.")
            continue

        try:
            a, b = float(a_str), float(b_str)
        except ValueError:
            print("Invalid numbers. Please enter valid numeric values.")
            continue

        try:
            # Perform the calculation using CalculationFactory
            calc = CalculationFactory.create(op, a, b)
            result = calc
