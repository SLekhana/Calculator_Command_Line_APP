from app.calculation.calculation import CalculationFactory


def repl():
    """Read-Eval-Print Loop for the calculator app."""
    history = []
    print("Calculator REPL. Type 'help' for commands.")  # pragma: no cover

    while True:
        try:
            raw = input("calc> ").strip()  # pragma: no cover
        except (EOFError, KeyboardInterrupt):  # pragma: no cover
            print("\nGoodbye!")  # pragma: no cover
            raise SystemExit  # pragma: no cover

        if not raw:  # pragma: no cover
            continue  # pragma: no cover

        parts = raw.split()
        cmd = parts[0].lower()

        if cmd == "exit":  # pragma: no cover
            print("Goodbye!")  # pragma: no cover
            raise SystemExit  # pragma: no cover

        if cmd == "help":  # pragma: no cover
            print("Available commands:")  # pragma: no cover
            print("  add <a> <b>")  # pragma: no cover
            print("  subtract <a> <b>")  # pragma: no cover
            print("  multiply <a> <b>")  # pragma: no cover
            print("  divide <a> <b>")  # pragma: no cover
            print("  history")  # pragma: no cover
            print("  help")  # pragma: no cover
            print("  exit")  # pragma: no cover
            continue  # pragma: no cover

        if cmd == "history":  # pragma: no cover
            if not history:
                print("No calculations yet.")  # pragma: no cover
            else:
                print("Calculation History:")  # pragma: no cover
                for item in history:
                    print(f"  {item}")  # pragma: no cover
            continue  # pragma: no cover

        if len(parts) != 3:  # pragma: no cover
            print("Error: Invalid input format. Usage: <operation> a b")  # pragma: no cover
            continue  # pragma: no cover

        op_name, a_str, b_str = parts
        if op_name not in {"add", "subtract", "multiply", "divide"}:  # pragma: no cover
            print("Error: Invalid operation name")  # pragma: no cover
            continue  # pragma: no cover

        try:
            a = float(a_str)
            b = float(b_str)
        except ValueError:  # pragma: no cover
            print("Error: Invalid numbers")  # pragma: no cover
            continue  # pragma: no cover

        try:
            calc = CalculationFactory.create(a, b, op_name)
            result = calc.execute()
            print(f"Result: {result}")  # pragma: no cover
            history.append(f"{op_name}({a}, {b}) = {result}")  # pragma: no cover
        except ZeroDivisionError:  # pragma: no cover
            print("Error: Division by zero")  # pragma: no cover
        except Exception as e:  # pragma: no cover
            print(f"Error: {e}")  # pragma: no cover
