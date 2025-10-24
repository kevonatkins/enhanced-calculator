# 🧮 Enhanced Calculator Command-Line Application
![CI](https://github.com/kevonatkins/enhanced-calculator/actions/workflows/python-app.yml/badge.svg)

### NJIT – IS601 / CS634 Midterm Project  
**Author:** Kevon Atkins  
**Due:** Friday 11:59 PM  
**Instructor:** Keith Williams

---

## Overview
This project implements an advanced, modular calculator built in Python with a **command-line REPL interface**, rich arithmetic operations, full error handling, data persistence, automated testing, and continuous integration via GitHub Actions. 

---

##  Project Structure
``` bash 
project_root/
├── app/
│ ├── init.py
│ ├── calculator.py
│ ├── calculation.py
│ ├── calculator_config.py
│ ├── calculator_memento.py
│ ├── exceptions.py
│ ├── history.py
│ ├── input_validators.py
│ ├── operations.py
│ ├── logger.py
│ └── observers.py
├── tests/
│ ├── test_calculator_core.py
│ ├── test_calculation.py
│ ├── test_operations.py
│ ├── test_history_basic.py
│ ├── test_observers.py
│ ├── test_commands.py
│ └── test_help_registry.py
├── .env
├── requirements.txt
├── README.md
└── .github/
└── workflows/
└── python-app.yml 
```

## Setup Instructions

### 1. Clone and enter project
```bash
git clone https://github.com/kevonatkins/enhanced-calculator.git
cd enhanced-calculator
```
## 2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```
## 3. Install dependencies


```bash
pip install -r requirements.txt
```
## Configuration (.env)
The calculator reads environment variables using python-dotenv.

| | | |
|:---|:---|:---| 
|Variable|Description|Example|
|`CALCULATOR_LOG_DIR`|directory for log files|`var/log` | 
|`CALCULATOR_HISTORY_DIR`	|directory for CSV history|	`var/history`|
|`CALCULATOR_MAX_HISTORY_SIZE`|	max number of saved operations|	`1000`|
|`CALCULATOR_AUTO_SAVE`|	auto-save on each calculation|	`true`|
|`CALCULATOR_PRECISION`|	decimal rounding precision|	`2`|
|`CALCULATOR_MAX_INPUT_VALUE`	|maximum allowed input value|`1000000`|
|`CALCULATOR_DEFAULT_ENCODING`|	encoding for I/O|	`utf-8`|

Default values are automatically provided if `.env` is missing.

## Usage Guide
Run the application:

```bash
python -m app.calculator
``` 
### Supported operations
`add`, `subtract`, `multiply`, `divide`, `power`, `root`, `modulus`, `int_divide`, `percent`, `abs_diff`

### Core commands

| | | 
|:---|:---|
|`Command`|	Description|
|`help`|	Display dynamic help menu|
|`history`|	Show past calculations|
|`clear`|	Clear history|
|`undo / redo`|	Undo or redo last operation|
|`save / load`|	Manually persist or restore history|
|`exit`| Exit program


## Example Session
```bash
> add 4 7
= 11
> power 2 8
= 256
> history
2025-10-24T15:42:19Z | add(4, 7) = 11
2025-10-24T15:42:25Z | power(2, 8) = 256
> undo
Undo done.
> redo
Redo done.
> save
History saved.
> exit
Bye!
``` 
## Design Patterns Implemented

| | | 
|:---|:---|
|**Pattern** |	Purpose|
|**Factory** |	Creates operation objects dynamically|
|**Memento** |	Enables undo/redo history management|
|**Observer** |	Logging and autosave triggered on new calculation|
|**Decorator** |	Registers commands and dynamically builds help menu|
|**Command** |	Encapsulates non-operation actions (help, undo, redo, etc.)|

##  Optional Features 
+ Dynamic Help Menu — Automatically lists all operations & commands
+ Command Pattern — REPL dispatches command objects cleanly
+ Color-Coded Output — Uses `colorama` for readable, user-friendly output

##  Testing

Run unit tests and view coverage:

```bash
pytest --cov=app --cov-report=term-missing
```
All tests must pass with ≥ 90 % coverage for CI to succeed.

## Continuous Integration (CI)
+ Every push and pull request to `main` triggers GitHub Actions:

+ Sets up Python 3.12

+ Installs dependencies

+ Runs pytest with coverage

+ Fails if coverage < 90 %

+ Uploads `.coverage` and `htmlcov` as build artifacts

+ Badge above shows live CI status.

## Logging & Persistence
+ Logs are stored in `var/log/calculator.log` with rotating handler.

+ History auto-saves to `var/history/history.csv` using pandas.

+ On restart, previous history is re-loaded automatically.

## Error Handling
+ Custom exceptions (`OperationError`, `ValidationError`, `PersistenceError`)

+ Graceful messages for invalid input, division by zero, or I/O issues

+ Input validation ensures numbers within configured limits

## Git Workflow
Development used isolated branches:

``` bash
feature/history-memento
feature/observer
feature/calculator-repl
feature/optional-help-command
ci/github-actions
```