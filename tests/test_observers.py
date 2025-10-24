import os
from pathlib import Path
from app.history import History
from app.calculation import Calculation
from app.observers import LoggingObserver, AutoSaveObserver
from app.calculator_config import load_config
from app.logger import get_logger

def test_logging_and_autosave_observers(tmp_path, monkeypatch):
    # point config dirs to temp
    monkeypatch.setenv("CALCULATOR_LOG_DIR", str(tmp_path / "log"))
    monkeypatch.setenv("CALCULATOR_HISTORY_DIR", str(tmp_path / "hist"))
    monkeypatch.setenv("CALCULATOR_DEFAULT_ENCODING", "utf-8")

    cfg = load_config()

    # ensure logger uses temp dir
    logger = get_logger()  # creates handler to tmp log path

    h = History(max_size=10)
    # register observers
    log_obs = LoggingObserver()
    auto_obs = AutoSaveObserver(h, cfg["CALCULATOR_HISTORY_FILE"], cfg["CALCULATOR_DEFAULT_ENCODING"])
    h.register_observer(log_obs)
    h.register_observer(auto_obs)

    # do a calculation and push
    c = Calculation("add", 2, 3); c.execute()
    h.push(c)

    # autosave CSV exists and has content
    csv_path = Path(cfg["CALCULATOR_HISTORY_FILE"])
    assert csv_path.exists() and csv_path.stat().st_size > 0

    # log file exists and contains operation info
    log_path = Path(cfg["CALCULATOR_LOG_FILE"])
    assert log_path.exists() and log_path.stat().st_size > 0
    content = log_path.read_text(encoding=cfg["CALCULATOR_DEFAULT_ENCODING"])
    assert "add" in content and "2" in content and "3" in content and "5" in content