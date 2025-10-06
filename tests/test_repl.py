import pytest
from app.calculator.repl import main

def test_help_command(monkeypatch, capsys):
    # Simulate user typing 'help' then 'exit'
    inputs = iter(["help", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        main()

    captured = capsys.readouterr()
    assert "Available commands" in captured.out

def test_invalid_command(monkeypatch, capsys):
    # Simulate invalid input then exit
    inputs = iter(["xyz", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        main()

    captured = capsys.readouterr()
    assert "Invalid command" in captured.out

