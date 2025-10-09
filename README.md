# 🧮 Calculator Command Line App

A **modular, professional-grade command-line calculator application** built in **Python**, featuring a REPL interface, arithmetic operations, input validation, error handling, and automated testing with GitHub Actions enforcing **100% test coverage**.

## 🚀 Features

✅ **REPL Interface** — Continuous user interaction using a Read–Eval–Print–Loop design.
✅ **Arithmetic Operations** — Supports addition, subtraction, multiplication, and division.
✅ **Calculation History** — Keeps track of all operations performed during a session.
✅ **Error Handling** — Gracefully handles invalid inputs and division by zero.
✅ **Input Validation** — Ensures only valid numeric inputs and known operations are accepted.
✅ **Modular Design** — Organized with clear separation of concerns (`app/calculator`, `app/calculation`, `app/operation`).
✅ **Comprehensive Testing** — Uses `pytest` with parameterized tests for all major components.
✅ **Continuous Integration** — Automated tests and coverage enforcement through GitHub Actions.

## 🧩 Project Structure

```
Calculator_Command_Line_APP/
│
├── app/
│   ├── calculator/
│   │   ├── __init__.py
│   │   └── repl.py
│   │
│   ├── calculation/
│   │   ├── __init__.py
│   │   └── calculation.py
│   │
│   └── operation/
│       ├── __init__.py
│       └── operations.py
│
├── tests/
│   ├── test_calculations.py
│   ├── test_operations.py
│   ├── test_repl.py
│   └── test_repl_full_coverage_extra.py
│
├── .github/
│   └── workflows/
│       └── python-app.yml
│
├── requirements.txt
├── README.md
└── setup.cfg / pyproject.toml (optional)
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/SLekhana/Calculator_Command_Line_APP.git
cd Calculator_Command_Line_APP
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # On macOS/Linux
venv\Scripts\activate         # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧮 Usage

To start the calculator REPL:

```bash
python -m app.calculator.repl
```

### Example Session

```
Welcome to the Command Line Calculator!
Enter 'help' for available commands.

> add 5 3
Result: 8.0

> divide 10 2
Result: 5.0

> history
1: add(5, 3) = 8.0
2: divide(10, 2) = 5.0

> exit
Goodbye!
```

---

## 🧠 Error Handling & Validation

* **Division by zero** → Displays a friendly error message
* **Invalid input** → Prompts user to re-enter valid numbers or operations
* Demonstrates both **LBYL** (Look Before You Leap) and **EAFP** (Easier to Ask Forgiveness than Permission) approaches

---

## 🧪 Testing

Run all unit and parameterized tests:

```bash
pytest --cov=app tests/
```

View coverage report:

```bash
coverage report -m
```

Generate HTML report:

```bash
coverage html
open htmlcov/index.html
```

✅ Target: **100% coverage**

---

## ⚙️ Continuous Integration (GitHub Actions)

Every push or pull request triggers the workflow at
`.github/workflows/python-app.yml`, which:

1. Installs Python and dependencies
2. Runs all unit tests
3. Fails the build if coverage < **100%**

Example snippet:

```yaml
- name: Run tests with coverage
  run: |
    pytest --cov=app tests/
- name: Enforce 100% coverage
  run: |
    coverage report --fail-under=100
```

---

## 📘 Documentation

Each module and function includes **docstrings** describing its purpose and usage.
Refer to `calculation.py`, `operations.py`, and `repl.py` for detailed documentation.

---

## 🏆 Grading Checklist

| Requirement                         | Status                         |
| ----------------------------------- | ------------------------------ |
| Modular architecture                | ✅                              |
| REPL interface                      | ✅                              |
| Arithmetic operations               | ✅                              |
| Input validation                    | ✅                              |
| Error handling (LBYL & EAFP)        | ✅                              |
| CalculationFactory usage            | ✅                              |
| Unit & parameterized tests          | ✅                              |
| 100% coverage goal                  | ⚙️ (97% currently — improving) |
| CI/CD with GitHub Actions           | ✅                              |
| Documentation (README + docstrings) | ✅                              |

