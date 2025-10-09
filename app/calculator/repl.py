from app.calculation.calculation import CalculationFactory

def repl():
    """Read-Eval-Print Loop for the calculator app."""
    history = []
    print("Calculator REPL. Type 'help' for commands.")

    while True:
        try:
            raw = input("calc> ").strip()
        except (EOFError, KeyboardInterrupt):  # pragma: no cover
            print("\nGoodbye!")
            raise SystemExit  # pragma: no cover

        if not raw:
            continue

        parts = raw.split()
        cmd = parts[0].lower()

        if cmd == "exit":
            print("Goodbye!")
            raise SystemExit  # pragma: no cover

        if cmd == "help":
            print("Available commands:")
            print("  add <a> <b>")
            print("  subtract <a> <b>")
            print("  multiply <a> <b>")
            print("  divide <a> <b>")
            print("  history")
            print("  help")
            print("  exit")
            continue

        if cmd == "history":
            if not history:
                print("No calculations yet.")
            else:
                print("Calculation History:")
                for item in history:
                    print(f"  {item}")
            continue

        if len(parts) != 3:
            print("Error: Invalid input format. Usage: <operation> a b")
            continue

        op_name, a_str, b_str = parts
        if op_name not in {"add", "subtract", "multiply", "divide"}:
            print("Error: Invalid operation name")
            continue

        try:
            a = float(a_str)
            b = float(b_str)
        except ValueError:
            print("Error: Invalid numbers")
            continue

        try:
            calc = CalculationFactory.create(a, b, op_name)
            result = calc.execute()
            print(f"Result: {result}")
            history.append(f"{op_name}({a}, {b}) = {result}")
        except ZeroDivisionError:
            print("Error: Division by zero")
        except Exception as e:  # pragma: no cover
            print(f"Error: {e}")
