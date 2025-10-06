import pytest
from app.calculator.repl import repl


def test_repl_runs_without_error(monkeypatch, capsys):
    """Simulate a full REPL session with valid operations and commands."""
    inputs = iter([
        "add 2 3",
        "subtract 10 4",
        "multiply 2 5",
        "divide 10 2",
        "history",
        "help",
        "exit",
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with pytest.raises(SystemExit):
        repl()

    out = capsys.readouterr().out
    assert "Calculator REPL. Type 'help' for commands." in out
    assert "Result: 5.0" in out        # add
    assert "Result: 6.0" in out        # subtract
    assert "Result: 10.0" in out       # multiply
    assert "Result: 5.0" in out        # divide
    assert "Available commands:" in out
    assert "Goodbye!" in out


def test_invalid_operation(monkeypatch, capsys):
    """Covers invalid operation command branch."""
    inputs = iter(["foo 1 2", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with pytest.raises(SystemExit):
        repl()
    out = capsys.readouterr().out
    assert "Invalid command" in out


def test_invalid_format(monkeypatch, capsys):
    """Covers wrong number of arguments (len(parts) != 3)."""
    inputs = iter(["add 1", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with pytest.raises(SystemExit):
        repl()
    out = capsys.readouterr().out
    assert "Invalid command" in out


def test_type_error_handling(monkeypatch, capsys):
    """Covers TypeError exception path in calculation execution."""
    from app.calculator import repl as repl_mod

    class DummyCalc:
        pass  # no execute(), perform(), or callable

    def bad_factory(*args, **kwargs):
        return DummyCalc()

    inputs = iter(["add 1 2", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr(
        repl_mod, "CalculationFactory", type("F", (), {"create": staticmethod(bad_factory)})
    )

    with pytest.raises(SystemExit):
        repl_mod.repl()

    out = capsys.readouterr().out
    assert "Error:" in out


def test_zero_division(monkeypatch, capsys):
    """Covers ZeroDivisionError branch."""
    inputs = iter(["divide 5 0", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with pytest.raises(SystemExit):
        repl()
    out = capsys.readouterr().out
    assert "Error: Division by zero" in out


def test_keyboard_interrupt(monkeypatch, capsys):
    """Covers KeyboardInterrupt path."""
    def raise_kb(_=None):
        raise KeyboardInterrupt

    monkeypatch.setattr("builtins.input", raise_kb)

    with pytest.raises(SystemExit):
        repl()

    out = capsys.readouterr().out
    assert "Goodbye!" in out


def test_eof(monkeypatch, capsys):
    """Covers EOFError path."""
    def raise_eof(_=None):
        raise EOFError

    monkeypatch.setattr("builtins.input", raise_eof)

    with pytest.raises(SystemExit):
        repl()

    out = capsys.readouterr().out
    assert "Goodbye!" in out


def test_empty_input(monkeypatch, capsys):
    """Covers case when user presses enter with no command."""
    inputs = iter(["", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with pytest.raises(SystemExit):
        repl()
    out = capsys.readouterr().out
    assert "Goodbye!" in out
