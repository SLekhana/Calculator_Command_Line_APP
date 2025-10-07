import pytest
from app.calculator import repl
from app.calculation.calculation import CalculationFactory
from app.operation import operations


def test_help_and_exit(monkeypatch, capsys):
    inputs = iter(["help", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    with pytest.raises(SystemExit):
        repl.repl()
    out = capsys.readouterr().out
    assert "Available commands" in out
    assert "Goodbye!" in out


def test_history_empty_and_after_ops(monkeypatch, capsys):
    inputs = iter(["history", "add 1 2", "history", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    with pytest.raises(SystemExit):
        repl.repl()
    out = capsys.readouterr().out
    assert "No calculations yet." in out
    assert "add(1.0, 2.0)" in out


def test_invalid_format_and_invalid_numbers(monkeypatch, capsys):
    inputs = iter(["add 1", "add a b", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    with pytest.raises(SystemExit):
        repl.repl()
    out = capsys.readouterr().out
    assert "Invalid input format" in out or "Invalid numbers" in out


def test_operations_and_zero_division(monkeypatch, capsys):
    inputs = iter(["add 2 3", "subtract 10 4", "multiply 2 5", "divide 10 2", "divide 5 0", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    with pytest.raises(SystemExit):
        repl.repl()
    out = capsys.readouterr().out
    assert "Result:" in out
    assert "Error: Division by zero" in out


def test_invalid_operation_name(monkeypatch, capsys):
    inputs = iter(["foobar 1 2", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    with pytest.raises(SystemExit):
        repl.repl()
    out = capsys.readouterr().out
    assert "Invalid operation name" in out


def test_keyboard_interrupt_and_eof(monkeypatch):
    # Simulate Ctrl+C
    monkeypatch.setattr("builtins.input", lambda _: (_ for _ in ()).throw(KeyboardInterrupt))
    with pytest.raises(SystemExit):
        repl.repl()

    # Simulate Ctrl+D
    monkeypatch.setattr("builtins.input", lambda _: (_ for _ in ()).throw(EOFError))
    with pytest.raises(SystemExit):
        repl.repl()


def test_calculation_factory_branches():
    c = CalculationFactory.create(2, 3, "add")
    assert c.execute() == 5

    c2 = CalculationFactory.create(20, 4, operations.divide)
    assert c2.perform() == 5

    with pytest.raises(ValueError):
        CalculationFactory.create(1, 1, "nope")

    c3 = CalculationFactory.create(5, 0, "divide")
    with pytest.raises(ZeroDivisionError):
        c3.perform()
