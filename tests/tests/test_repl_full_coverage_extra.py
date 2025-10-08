import builtins
import pytest
from app.calculator import repl
from app.calculation.calculation import Calculation
from app.operation import operations

# --- Tests for repl.py missing lines ---

def test_repl_quit(monkeypatch, capsys):
    """Covers the quit path."""
    inputs = iter(["quit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    repl.run_repl()
    captured = capsys.readouterr()
    assert "Goodbye" in captured.out


def test_repl_invalid_input(monkeypatch, capsys):
    """Covers invalid command handling."""
    inputs = iter(["invalid input", "quit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    repl.run_repl()
    captured = capsys.readouterr()
    assert "Invalid" in captured.out or "Error" in captured.out


def test_repl_divide_by_zero(monkeypatch, capsys):
    """Covers division by zero edge case."""
    inputs = iter(["divide 5 0", "quit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    repl.run_repl()
    captured = capsys.readouterr()
    assert "Error" in captured.out or "Cannot divide by zero" in captured.out


# --- Tests for calculation.py missing lines ---

def test_calculation_repr_and_str():
    """Covers __repr__ and __str__ in Calculation."""
    calc = Calculation(3, 4, operations.add)
    assert "Calculation" in repr(calc)
    assert "3" in str(calc)


def test_calculation_static_methods():
    """Covers edge methods for full calculation coverage."""
    add_calc = Calculation(2, 3, operations.add)
    sub_calc = Calculation(5, 2, operations.subtract)
    mul_calc = Calculation(2, 3, operations.multiply)
    div_calc = Calculation(6, 3, operations.divide)
    assert add_calc.get_result() == 5
    assert sub_calc.get_result() == 3
    assert mul_calc.get_result() == 6
    assert div_calc.get_result() == 2

