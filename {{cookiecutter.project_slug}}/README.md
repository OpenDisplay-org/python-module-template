# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

[![Tests](https://github.com/OpenDisplay-org/{{cookiecutter.project_slug}}/actions/workflows/test.yml/badge.svg)](https://github.com/OpenDisplay-org/{{cookiecutter.project_slug}}/actions/workflows/test.yml)
[![PyPI](https://img.shields.io/pypi/v/{{cookiecutter.project_slug}})](https://pypi.org/project/{{cookiecutter.project_slug}}/)
[![Python Version](https://img.shields.io/pypi/pyversions/{{cookiecutter.project_slug}})](https://pypi.org/project/{{cookiecutter.project_slug}}/)

## Installation

```bash
pip install {{cookiecutter.project_slug}}
```

## Quick Start

```python
# TODO: Add a simple usage example
import {{cookiecutter.package_name}}

# Example usage here
```

## Features

<!-- TODO: List key features -->
- Feature 1
- Feature 2
- Feature 3

## Usage

### Basic Example

```python
# TODO: Add detailed usage examples
```

### Advanced Usage

<!-- TODO: Document advanced features -->

## API Reference

<!-- TODO: Document main classes, functions, and parameters -->

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/OpenDisplay-org/{{cookiecutter.project_slug}}.git
cd {{cookiecutter.project_slug}}

# Install with all dependencies
uv sync --all-extras
```

### Running Tests

```bash
# Run all tests
uv run pytest tests/ -v

# Run with coverage
uv run pytest tests/ --cov=src/{{cookiecutter.package_name}}

# Run specific test file
uv run pytest tests/test_specific.py -v
```

### Code Quality

```bash
# Lint code
uv run ruff check .

# Format code (if ruff format is configured)
uv run ruff format .

# Type check
uv run mypy src/{{cookiecutter.package_name}}
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linting
5. Commit using conventional commits (`feat:`, `fix:`, etc.)
6. Push to your fork
7. Open a Pull Request
