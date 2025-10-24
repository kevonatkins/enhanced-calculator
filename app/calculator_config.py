import os
from pathlib import Path
from dotenv import load_dotenv 
from typing import Any, Dict 

DEFAULTS = {
    "CALCULATOR_LOG_DIR": "var/log",
    "CALCULATOR_HISTORY_DIR": "var/history",
    "CALCULATOR_MAX_HISTORY_SIZE": "1000",
    "CALCULATOR_AUTO_SAVE": "true",
    "CALCULATOR_PRECISION": "6",
    "CALCULATOR_MAX_INPUT_VALUE": "1e12",
    "CALCULATOR_DEFAULT_ENCODING": "utf-8",
}

def load_config() -> Dict[str, Any]:
    load_dotenv()
    cfg: Dict[str, Any] = {k: os.getenv(k, v) for k, v in DEFAULTS.items()}

    # ensure dirs exist
    log_dir = Path(cfg["CALCULATOR_LOG_DIR"]); log_dir.mkdir(parents=True, exist_ok=True)
    hist_dir = Path(cfg["CALCULATOR_HISTORY_DIR"]); hist_dir.mkdir(parents=True, exist_ok=True)

    # derive file paths
    cfg["CALCULATOR_LOG_FILE"] = str(log_dir / "calculator.log")
    cfg["CALCULATOR_HISTORY_FILE"] = str(hist_dir / "history.csv")

    # cast types
    cfg["CALCULATOR_AUTO_SAVE"] = str(cfg["CALCULATOR_AUTO_SAVE"]).lower() == "true"
    cfg["CALCULATOR_MAX_HISTORY_SIZE"] = int(float(cfg["CALCULATOR_MAX_HISTORY_SIZE"]))
    cfg["CALCULATOR_PRECISION"] = int(float(cfg["CALCULATOR_PRECISION"]))
    cfg["CALCULATOR_MAX_INPUT_VALUE"] = float(cfg["CALCULATOR_MAX_INPUT_VALUE"])
    return cfg