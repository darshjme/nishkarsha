# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.x     | ✅ Yes    |

## Scope

`agent-extractor` is a pure-Python text processing library with no network access,
no file I/O, and no external dependencies. Its attack surface is limited to:

- **ReDoS (Regular Expression Denial of Service):** malicious input strings designed
  to cause catastrophic backtracking in regex patterns.

## Reporting a Vulnerability

Please **do not** open a public GitHub issue for security vulnerabilities.

Email: **darshjme@gmail.com** with subject `[SECURITY] agent-extractor`

Include:
- Description of the vulnerability
- Reproduction steps (input that triggers the issue)
- Python version and OS
- Estimated severity

You will receive a response within **72 hours**.

## ReDoS Mitigation

All regex patterns in this library are reviewed to avoid unbounded quantifier
combinations on overlapping character classes. If you discover a pattern that
causes super-linear backtracking, please report it immediately.
