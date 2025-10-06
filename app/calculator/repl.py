"""
Simple REPL that uses CalculationFactory from app.calculation.
The __main__ guard is excluded from coverage.
"""
from app.calculation import CalculationFactory

def print_help():
    print("Commands: help | history | exit")
    print("Usage: <operation> <num1> <num2>")
    print("Operations: add, subtract, multiply, divide")

def repl():
    history = []
    print("Calculator REPL. Type 'help' for commands.")
    while True:
        try:
            raw = input("calc> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye")
            break
        if not raw:
            continue
        parts = raw.split()
        cmd = parts[0].lower()
        if cmd in ("exit", "quit"):
            print("Goodbye")
            break
        if cmd == "help":
            print_help()
            continue
        if cmd == "history":
            if not history:
                print("No history.")
            else:
                for i, h in enumerate(history, 1):
                    print(f"{i}: {h}")
            continue

       
        op = cmd
        operands = parts[1:]
  
        if len(operands) < 1:
            print("Error: provide at least one operand (e.g. add 1 2)")
            continue
       
        try:
            nums = []
            for t in operands:
                if "." in t:
                    nums.append(float(t))
                else:
                    nums.append(int(t))
            calc = CalculationFactory.create(nums[0], nums[1] if len(nums) > 1 else 0, op) if len(nums)==2 else CalculationFactory.create(nums[0], nums[1] if len(nums)>1 else 0, op)
            result = calc.execute()
            print("Result:", result)
            history.append(f"{op} {operands} = {result}")
        except Exception as exc:
            print("Error:", exc)

if __name__ == "__main__":  
    repl()
