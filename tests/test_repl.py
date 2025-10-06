import pytest
from app.calculator.repl import repl, main


def test_help_command(monkeypatch, capsys):
    """Simulate 'help' then 'exit'."""
    inputs = iter(["help", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Expect SystemExit on 'exit'
    with pytest.raises(SystemExit):
        main()

    captured = capsys.readouterr()
    assert "Available commands" in captured.out
    assert "Operations: add, subtract, multiply, divide" in captured.out
    assert "Goodbye!" in captured.out


def test_invalid_command(monkeypatch, capsys):
    """Simulate invalid input and exit."""
    inputs = iter(["xyz", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with pytest.raises(SystemExit):
        main()

    captured = capsys.readouterr()
    assert "Invalid command" in captured.out
    assert "Goodbye!" in captured.out


def test_repl_runs_without_error(monkeypatch, capsys):
    """Simulate full REPL session with valid operations."""
    inputs = iter([
        "add 2 3",
        "subtract 10 4",
        "multiply 2 5",
        "divide 10 2",
        "history",
        "help",
        "exit"
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Expect clean exit from REPL
    with pytest.raises(SystemExit):
        repl()

    captured = capsys.readouterr()

    # Validate all expected outputs
    assert "Calculator REPL. Type 'help' for commands." in captured.out
    assert "Result: 5.0" in captured.out       # add
    assert "Result: 6.0" in captured.out       # subtract
    assert "Result: 10.0" in captured.out      # multiply
    assert "Result: 5.0" in captured.out       # divide
    assert "History:" in captured.out
    assert "Available commands" in captured.out
    assert "Goodbye!" in captured.out
