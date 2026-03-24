"""DateExtractor — extract date strings in common formats."""

import re

_MONTHS_LONG = (
    "January|February|March|April|May|June|July|August|"
    "September|October|November|December"
)
_MONTHS_SHORT = "Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec"

# Order matters — more specific patterns first
_DATE_PATTERNS = [
    # ISO: 2026-01-25
    re.compile(r"\b(\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01]))\b"),
    # DD/MM/YYYY or MM/DD/YYYY — both captured (ambiguous but valid)
    re.compile(r"\b((?:0?[1-9]|[12]\d|3[01])/(?:0?[1-9]|1[0-2])/\d{4})\b"),
    # "Jan 25 2026" or "Jan 25, 2026"
    re.compile(
        r"\b((?:" + _MONTHS_SHORT + r")\s+\d{1,2},?\s+\d{4})\b",
        re.IGNORECASE,
    ),
    # "25 January 2026"
    re.compile(
        r"\b(\d{1,2}\s+(?:" + _MONTHS_LONG + r")\s+\d{4})\b",
        re.IGNORECASE,
    ),
    # "January 25, 2026" or "January 25 2026"
    re.compile(
        r"\b((?:" + _MONTHS_LONG + r")\s+\d{1,2},?\s+\d{4})\b",
        re.IGNORECASE,
    ),
]


class DateExtractor:
    """Extract date strings from unstructured text."""

    def extract(self, text: str) -> list[str]:
        """Return all date strings found in *text*, preserving order, deduped."""
        seen: set[str] = set()
        # Track positions to avoid overlapping matches
        covered: list[tuple[int, int]] = []
        matches: list[tuple[int, int, str]] = []

        for pat in _DATE_PATTERNS:
            for m in pat.finditer(text):
                start, end = m.start(), m.end()
                # Skip if overlaps with an already-found match
                if any(s <= start < e or s < end <= e for s, e in covered):
                    continue
                date_str = m.group(1)
                if date_str not in seen:
                    seen.add(date_str)
                    covered.append((start, end))
                    matches.append((start, end, date_str))

        matches.sort(key=lambda x: x[0])
        return [m[2] for m in matches]
