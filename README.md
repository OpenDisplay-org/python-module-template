# OpenDisplay Python Module Template

A cookiecutter template for creating Python packages.

## Features

- Modern Python packaging (PEP 517/621) with hatchling
- uv for fast dependency management
- GitHub Actions CI/CD (test, lint, release)
- Automated releases with release-please
- PyPI publishing with trusted publishing
- Pre-configured ruff (linting) and mypy (type checking)
- Python 3.11, 3.12, 3.13 test matrix

## Quick Start

```bash
# Generate new project
uvx cookiecutter gh:OpenDisplay/python-module-template

# Follow interactive prompts, then:
cd your-project-name
git init && git add . && git commit -m "chore: initial commit"
uv sync --all-extras
```


## Configuration

Cookiecutter will prompt for the following values:

| Prompt | Default | Description |
|--------|---------|-------------|
| `project_name` | `My Python Package` | Human-readable project name |
| `project_slug` | _(derived)_ | PyPI package name (auto-generated from project name) |
| `package_name` | _(derived)_ | Python import name (auto-generated from slug) |
| `project_short_description` | `A Python package` | One-line description |
| `github_username` | `OpenDisplay` | GitHub user or org that will host the repo |
| `author_name` | `g4bri3lDev` | Author name for pyproject.toml |
| `author_email` | `admin@g4bri3l.de` | Author email for pyproject.toml |
| `version` | `0.1.0` | Initial version |
| `python_version` | `3.11` | Minimum Python version |
| `license` | `Apache-2.0` | License (Apache-2.0, MIT, or GPL-3.0) |

## After Generation

1. **Create GitHub repository**: At `github_username/your-project-slug`
2. **Configure PyPI trusted publishing**: In PyPI project settings
3. **Push initial commit**: `git remote add origin ... && git push -u origin main`
4. **Start developing**: Add code to `src/package_name/`
5. **Write tests**: Add tests to `tests/`
6. **Update README**: Customize the generated README.md
7. **First release**: Commit using conventional commits (feat:, fix:, etc.)

## Development Commands

```bash
# Install with all dependencies
uv sync --all-extras

# Run tests
uv run pytest tests/ -v

# Run tests with coverage
uv run pytest tests/ --cov=src/package_name

# Lint code
uv run ruff check .

# Type check
uv run mypy src/package_name
```

## Conventional Commits

Use conventional commit messages for automatic versioning:

- `feat:` - New feature (minor version bump)
- `fix:` - Bug fix (patch version bump)
- `feat!:` or `fix!:` - Breaking change (major version bump)
- `docs:`, `refactor:`, `test:`, `chore:` - No version bump
