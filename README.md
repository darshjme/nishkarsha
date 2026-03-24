# agent-extractor

**Structured data extraction from unstructured text. Zero dependencies. Pure Python.**

Built for AI agents that receive raw text and need to pull out emails, URLs, dates, numbers, or any custom pattern — reliably, without writing fragile one-off regex.

```
pip install agent-extractor
```

---

## Quick Start — Agent Text Extraction

```python
from agent_extractor import (
    EmailExtractor,
    UrlExtractor,
    NumberExtractor,
    DateExtractor,
    PatternExtractor,
)

# Simulate an agent receiving unstructured text
report = """
    Project Alpha Status — March 2026

    Contact: sarah@company.com, ops@company.org
    Dashboard: https://dashboard.company.com/alpha
    Docs: https://docs.company.com

    Sprint velocity: 42 story points
    Code coverage: 87.3%
    Response time: 120ms
    Database size: 4.7GB

    Sprint started: 2026-03-01
    Demo day: March 25, 2026
    Deadline: 25/03/2026
"""

# Extract emails
emails = EmailExtractor().extract(report)
# → ['sarah@company.com', 'ops@company.org']

# Extract URLs
urls = UrlExtractor().extract(report)
# → ['https://dashboard.company.com/alpha', 'https://docs.company.com']

# Extract domains
domains = UrlExtractor().extract_domains(report)
# → ['dashboard.company.com', 'docs.company.com']

# Extract numbers with units
numbers = NumberExtractor().extract(report)
# → [
#     {'value': 42.0,   'unit': None,  'raw': '42'},
#     {'value': 87.3,   'unit': '%',   'raw': '87.3%'},
#     {'value': 120.0,  'unit': 'ms',  'raw': '120ms'},
#     {'value': 4.7,    'unit': 'GB',  'raw': '4.7GB'},
#   ]

# Extract dates
dates = DateExtractor().extract(report)
# → ['2026-03-01', 'March 25, 2026', '25/03/2026']

# Custom pattern — hashtags
tags = PatternExtractor(r"#\w+").extract("Status: #done #blocked #review")
# → ['#done', '#blocked', '#review']
```

---

## API Reference

### `EmailExtractor`

| Method | Returns | Description |
|--------|---------|-------------|
| `extract(text)` | `list[str]` | All unique emails, lowercased |
| `extract_first(text)` | `str \| None` | First email found |
| `is_valid(email)` | `bool` | RFC-style validation |

### `UrlExtractor`

| Method | Returns | Description |
|--------|---------|-------------|
| `extract(text)` | `list[str]` | All unique http/https/ftp URLs |
| `extract_domains(text)` | `list[str]` | Unique domain names |
| `extract_first(text)` | `str \| None` | First URL found |

### `NumberExtractor`

| Method | Returns | Description |
|--------|---------|-------------|
| `extract(text)` | `list[dict]` | `{value, unit, raw}` per number |
| `extract_integers(text)` | `list[int]` | Only whole numbers |
| `extract_floats(text)` | `list[float]` | All numbers as floats |

### `DateExtractor`

| Method | Returns | Description |
|--------|---------|-------------|
| `extract(text)` | `list[str]` | Raw date strings in order found |

**Formats recognized:** `YYYY-MM-DD`, `DD/MM/YYYY`, `MM/DD/YYYY`, `Jan 25 2026`, `25 January 2026`, `January 25, 2026`

### `PatternExtractor`

```python
PatternExtractor(pattern: str, group: int = 0, flags: int = 0)
```

| Method | Returns | Description |
|--------|---------|-------------|
| `extract(text)` | `list[str]` | All matches (or capture group) |
| `extract_first(text)` | `str \| None` | First match |

---

## Design Principles

- **Zero dependencies** — only Python's built-in `re` module
- **Deterministic** — same input always produces same output
- **Order-preserving** — results appear in the order found in text
- **Deduplication** — no repeated matches
- **Composable** — mix and match extractors freely

---

## Development

```bash
git clone https://github.com/darshjme-codes/agent-extractor
cd agent-extractor
pip install -e ".[dev]"
pytest tests/ -v
```

---

## License

MIT © 2026 Darshankumar Joshi
