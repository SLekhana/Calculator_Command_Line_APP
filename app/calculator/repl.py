"""
Command-line REPL for the calculator.
Implements CalculationFactory and supports commands: help, history, exit.
"""
from app.calculation import CalculationFactory


def print_help():
    """Display available commands and usage instructions."""
    print("Available commands:")
    print("  help    - Show this message")
    print("  history - Show past calculations")
    print("  exit    - Exit the calculator")
    print("Usage:")
    print("  <operation> <num1> <num2>")
    print("  Operations: add, subtract, multiply, divide")


def execute_command(raw_input, history):
    """Execute a single user command (for testing and REPL loop)."""
    parts = raw_input.split()
    if not parts:
        return "Invalid input. Try again or type 'help'."

    cmd = parts[0].lower()

    # Command handling
    if cmd == "help":
        print_help()
        return "help_shown"
    elif cmd == "history":
        if history:
            print("\n".join(str(item) for item in history))
        else:
            print("No history yet.")
        return "history_shown"
    elif cmd == "exit":
        print("Goodbye!")
        raise SystemExit

    # Operation handling
    if len(parts) != 3:
        return "Invalid input. Try again or type 'help'."

    operation, num1, num2 = parts
    try:
        num1, num2 = float(num1), float(num2)
    except ValueError:
        return "Invalid input. Try again or type 'help'."

    try:
        calculation = CalculationFactory.create(operation, num1, num2)
        result = calculation.perform()
        history.append(f"{operation}({num1}, {num2}) = {result}")
        print(f"Result: {result}")
        return "success"
    except Exception as e:  # pragma: no cover (safety net)
        print(f"Error: {e}")
        return "error"


def repl():
    """Main Read-Eval-Print Loop for the calculator."""
    history = []
    print("Calculator REPL. Type 'help' for commands.")
    while True:
        try:
            raw = input("calc> ").strip()
            execute_command(raw, history)
        except (EOFError, KeyboardInterrupt):  # pragma: no cover
            print("\nGoodbye!")
            break
        except SystemExit:
            break


if __name__ == "__main__":  # pragma: no cover
    repl()

# Alias for testing
main = repl  # used by test_repl.py
