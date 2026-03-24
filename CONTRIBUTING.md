# Contributing to agent-extractor

Thank you for your interest in contributing!

## Getting Started

```bash
git clone https://github.com/darshjme-codes/agent-extractor
cd agent-extractor
pip install -e ".[dev]"
```

## Guidelines

- **Zero dependencies** — contributions must not add external dependencies; use `re` only
- **Tests required** — every new feature or bug fix must include a test
- **Python 3.10+** — use modern type hints (`list[str]`, `str | None`)
- **Deterministic** — extractors must produce identical output for identical input

## Running Tests

```bash
pytest tests/ -v
```

## Submitting Changes

1. Fork the repository
2. Create a branch: `git checkout -b feature/my-feature`
3. Add tests for your change
4. Run the test suite and ensure all pass
5. Open a pull request with a clear description

## Reporting Bugs

Open an issue with:
- Python version
- Input text that caused unexpected behavior
- Expected output vs actual output

## Code Style

- Use `black` for formatting (optional but appreciated)
- Keep methods focused and single-purpose
- Docstrings for all public methods
