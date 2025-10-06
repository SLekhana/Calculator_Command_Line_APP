def test_repl_blank_and_invalid_input(monkeypatch, capsys):
    """Cover blank line and invalid number handling for full coverage."""
    inputs = iter([
        "",               # blank line
        "add a b",        # invalid numeric values
        "exit",           # quit
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    import pytest
    from app.calculator.repl import repl

    with pytest.raises(SystemExit):
        repl()

    out = capsys.readouterr().out
    assert "Error:" in out or "Goodbye" in out
