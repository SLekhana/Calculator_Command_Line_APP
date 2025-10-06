"""Command-line REPL for the Calculator application."""

from app.calculation.calculation import CalculationFactory


def repl():
    """Run the calculator REPL loop."""
    history = []
    print("Calculator REPL. Type 'help' for commands.")

    while True:
        try:
            user_input = input(">>> ").strip()
            if not user_input:
                continue

            parts = user_input.split()
            command = parts[0].lower()

            if command == "exit":
                print("Goodbye!")
                raise SystemExit

            elif command == "help":
                print("Available commands:")
                print("  add a b        - Add two numbers")
                print("  subtract a b   - Subtract two numbers")
                print("  multiply a b   - Multiply two numbers")
                print("  divide a b     - Divide two numbers")
                print("  history        - Show calculation history")
                print("  help           - Show this help message")
                print("  exit           - Exit the calculator")

            elif command == "history":
                if not history:
                    print("No calculations yet.")
                else:
                    print("Calculation History:")
                    for item in history:
                        print(f"  {item}")

            elif command in {"add", "subtract", "multiply", "divide"}:
                if len(parts) != 3:
                    print("Error: Invalid input format. Usage: <operation> a b")
                    continue

                try:
                    a, b = float(parts[1]), float(parts[2])
                except ValueError:
                    print("Error: Invalid numbers")
                    continue

                try:
                    calc = CalculationFactory.create(a, b, command)
                    result = calc.execute()
                    print(f"Result: {result}")
                    history.append(f"{command}({a}, {b}) = {result}")
                except ZeroDivisionError:
                    print("Error: Division by zero")
                except ValueError as e:
                    print(f"Error: {e}")

            else:
                print("Error: Invalid input format. Type 'help' for commands.")

        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            raise SystemExit
