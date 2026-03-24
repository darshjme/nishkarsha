# Changelog

All notable changes to **agent-extractor** will be documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows [Semantic Versioning](https://semver.org/).

---

## [1.0.0] — 2026-03-25

### Added
- `EmailExtractor` — extract and validate RFC-style email addresses
- `UrlExtractor` — extract http/https/ftp URLs and domain names
- `NumberExtractor` — extract numbers with optional units (kg, ms, %, °C, etc.)
- `DateExtractor` — extract dates in ISO, slash, and natural-language formats
- `PatternExtractor` — custom regex extraction with capture-group support
- 25+ pytest tests with 100% scenario coverage
- Zero external dependencies (pure `re` module)
- Python 3.10+ support

[1.0.0]: https://github.com/darshjme-codes/agent-extractor/releases/tag/v1.0.0
