from app.operation.operations import add, subtract, multiply, divide
from app.calculation.calculation import Calculation


def repl():
    """Run the Read-Eval-Print Loop for the calculator."""
    history = []
    print("Calculator REPL. Type 'help' for commands.")

    while True:
        try:
            raw = input("calc> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            raise SystemExit

        if not raw:
            continue

        # Exit command
        if raw.lower() == "exit":
            print("Goodbye!")
            raise SystemExit

        # Help command
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

        # History command
        if raw.lower() == "history":
            if not history:
                print("No calculations yet.")
            else:
                print("History:")
                for item in history:
                    print(f"  {item}")
            continue

        # Handle operations
        parts = raw.split()
        if len(parts) == 3:
            op, a_str, b_str = parts
            try:
                a, b = float(a_str), float(b_str)
            except ValueError:
                print("Invalid numbers. Usage: <operation> <num1> <num2>")
                continue

            operation_map = {
                "add": add,
                "subtract": subtract,
                "multiply": multiply,
                "divide": divide,
            }

            func = operation_map.get(op.lower())
            if func:
                result = func(a, b)
                history.append(Calculation(a, b, func))
                print(f"Result: {result}")
            else:
                print("Invalid command. Try again or type 'help'.")
        else:
            print("Invalid command. Try again or type 'help'.")


def main():
    """Entry point for running REPL."""
    repl()


if __name__ == "__main__":
    main()
