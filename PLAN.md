# pseudo — plan

A CLI tool that renders text as ASCII art in your terminal.

## Usage

```
pseudo hello              → renders "hello" in default style (roman)
pseudo -roman hello       → renders "hello" in roman style
pseudo -styles            → lists all available styles
```

## Styles

| Flag      | Font name | Status      |
| --------- | --------- | ----------- |
| (default) | roman     | ✅ included |
| `-roman`  | roman     | ✅ included |

More styles can be added later by extending the styles registry.

## Installation

Packaged as a Python package using `pyproject.toml`.

Install globally with:

```
pip install .
```

After install, `pseudo` is available in the terminal forever — no need to activate
any environment, works on every new terminal session.

## Project structure

```
pseudo/
├── pyproject.toml        # package config + entry point
├── pseudo/
│   ├── __init__.py
│   └── cli.py            # all logic lives here
└── PLAN.md
```

## Implementation notes

- Uses `pyfiglet` for ASCII rendering
- Uses `colorama` for cross-platform terminal compatibility
- Entry point: `pseudo` → calls `pseudo.cli:main`
- `pseudo -styles` prints a numbered list of available style names
- Unknown flags print a short usage hint
