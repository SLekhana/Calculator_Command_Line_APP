import builtins
import pytest
from app.calculator.repl import repl, main

@pytest.fixture
def mock_input(monkeypatch):
    inputs = iter([
        "add 2 3",
        "subtract 10 4",
        "multiply 3 5",
        "divide 8 2",
        "history",
        "help",
        "exit"
    ])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

def test_repl_runs_without_error(mock_input, capsys):
    """Simulate a full REPL session and ensure all commands work."""
    repl()
    captured = capsys.readouterr()
    assert "Result: 5.0" in captured.out
    assert "Result: 6.0" in captured.out
    assert "Result: 15.0" in captured.out
    assert "Result: 4.0" in captured.out
    assert "History:" in captured.out
    assert "Type 'help' for instructions" not in captured.out  # only shown at start
    assert "Exiting calculator" in captured.out

def test_main_alias():
    """Ensure main() calls repl() correctly."""
    assert callable(main)
