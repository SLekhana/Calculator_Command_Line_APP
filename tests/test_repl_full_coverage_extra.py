import pytest
from app.calculator import repl
from app.calculation.calculation import Calculation
from app.operation import operations


def test_repl_exit_command(monkeypatch, capsys):
    """Test the exit command."""
    inputs = iter(["exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    with pytest.raises(SystemExit):
        repl.repl()
    output = capsys.readouterr().out
    assert "Calculator REPL" in output
    assert "Goodbye!" in output


def test_repl_invalid_operation_command(monkeypatch, capsys):
    """Test invalid operation command handling."""
    inputs = iter(["invalid 1 2", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    with pytest.raises(SystemExit):
        repl.repl()
    output = capsys.readouterr().out
    assert "Invalid operation name" in output


def test_repl_divide_by_zero(monkeypatch, capsys):
    """Test division by zero edge case."""
    inputs = iter(["divide 5 0", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    with pytest.raises(SystemExit):
        repl.repl()
    output = capsys.readouterr().out
    assert "Division by zero" in output


def test_calculation_perform_methods():
    """Test perform() method for all operation types."""
    add_calc = Calculation(2, 3, operations.add)
    sub_calc = Calculation(5, 2, operations.subtract)
    mul_calc = Calculation(2, 3, operations.multiply)
    div_calc = Calculation(6, 3, operations.divide)

    assert add_calc.perform() == 5
    assert sub_calc.perform() == 3
    assert mul_calc.perform() == 6
    assert div_calc.perform() == 2


def test_repl_help_command(monkeypatch, capsys):
    """Test the help command."""
    inputs = iter(["help", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    with pytest.raises(SystemExit):
        repl.repl()
    output = capsys.readouterr().out
    assert "Available commands" in output
