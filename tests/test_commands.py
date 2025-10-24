from app.calculator import Calculator, HelpCommand, ClearCommand

def test_commands_execute(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("CALCULATOR_LOG_DIR", str(tmp_path / "log"))
    monkeypatch.setenv("CALCULATOR_HISTORY_DIR", str(tmp_path / "hist"))

    calc = Calculator()
    # Help prints a menu
    HelpCommand().execute(calc)
    out = capsys.readouterr().out
    assert "Operations:" in out and "Commands:" in out

    # Clear prints a confirmation
    ClearCommand().execute(calc)
    out = capsys.readouterr().out
    assert "History cleared." in out