# HelloWorld

A simple Python package for greeting the world and people! This project demonstrates modern Python packaging practices using the `src/` layout.

## Features

- Simple `hello_world()` function that prints "Hello, World!"
- Personalized `greet(name)` function with input validation
- Command-line interface
- Comprehensive test suite with pytest
- Modern Python tooling (Black, Flake8, MyPy)
- Coverage reporting

## Installation

### From source
```bash
git clone <your-repo-url>
cd helloworld
pip install -e .
```

### For development
```bash
git clone <your-repo-url>
cd helloworld
pip install -e ".[dev]"
# Or alternatively:
pip install -r requirements-dev.txt
```

## Usage

### As a Python package
```python
from helloworld import hello_world, greet

# Simple hello world
hello_world()  # Prints: Hello, World!

# Personalized greeting
greet("Alice")  # Prints: Hello, Alice!
```

### As a command-line tool
After installation, you can use the `helloworld` command:
```bash
helloworld
```

### Direct execution
You can also run the module directly (after installation):
```bash
python -m helloworld.main
```

## Development

### Setup
```bash
# Install in development mode with all dev dependencies
pip install -e ".[dev]"
```

### Running tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=helloworld

# Run with verbose output
pytest -v
```

### Code quality

#### Formatting
```bash
black .
```

#### Linting
```bash
flake8
```

#### Type checking
```bash
mypy src/
```

#### All quality checks
```bash
black . && flake8 && mypy src/ && pytest
```

## Project Structure

```
helloworld/
├── README.md
├── requirements.txt
├── requirements-dev.txt
├── setup.py
├── pyproject.toml
├── src/
│   └── helloworld/
│       ├── __init__.py
│       └── main.py
└── tests/
    ├── __init__.py
    └── test_main.py
```

## Why src/ layout?

This project uses the `src/` layout, which is considered a best practice because:

- **Prevents accidental imports**: You must install the package to test it
- **Cleaner separation**: Source code is clearly separated from configuration
- **Better for packaging**: Reduces packaging mistakes and import issues
- **Industry standard**: Used by most modern Python projects

## License

This project is licensed under the MIT License.