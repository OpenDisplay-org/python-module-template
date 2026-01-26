#!/usr/bin/env python
"""Post-generation hook for cookiecutter template."""
import os

# Could add validation or cleanup here
# Example: Remove Python 2 specific files, validate package name, etc.

print("✅ Project generated successfully!")
print(f"📁 Project: {os.getcwd()}")
print("\n📝 Next steps:")
print("  1. cd {{cookiecutter.project_slug}}")
print("  2. git init && git add . && git commit -m 'chore: initial commit'")
print("  3. uv sync --all-extras")
print("  4. Start coding!")
