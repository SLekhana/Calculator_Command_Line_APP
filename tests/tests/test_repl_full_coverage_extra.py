import builtins
import pytest
from app.calculator import repl
from app.calculation.calculation import Calculation
from app.operation import operations


def test_repl_quit(monkeypatch, capsys):
    """Covers the quit path safely without StopIteration."""
    inputs = iter(["quit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs, "quit"))
    repl.repl()
    output = capsys.readouterr().out
    assert "Calculator REPL" in output


def test_repl_invalid_input(monkeypatch, capsys):
    """Covers invalid command handling without StopIteration."""
    inputs = iter(["invalid input", "quit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs, "quit"))
    repl.repl()
    output = capsys.readouterr().out
    assert "Invalid input" in output


def test_repl_divide_by_zero(monkeypatch, capsys):
    """Covers division by zero edge case."""
    inputs = iter(["divide 5 0", "quit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs, "quit"))
    repl.repl()
    output = capsys.readouterr().out
    assert "Division by zero" in output


def test_calculation_perform_methods():
    """Covers perform() for all operation types."""
    add_calc = Calculation(2, 3, operations.add)
    sub_calc = Calculation(5, 2, operations.subtract)
    mul_calc = Calculation(2, 3, operations.multiply)
    div_calc = Calculation(6, 3, operations.divide)

    assert add_calc.perform() == 5
    assert sub_calc.perform() == 3
    assert mul_calc.perform() == 6
    assert div_calc.perform() == 2


def test_repl_help(monkeypatch, capsys):
    """Covers help command."""
    inputs = iter(["help", "quit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs, "quit"))
    repl.repl()
    output = capsys.readouterr().out
    assert "Available operations" in output
