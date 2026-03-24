"""EmailExtractor — extract and validate email addresses."""

import re
from typing import Optional

# RFC 5322-inspired pattern (practical subset)
_EMAIL_PATTERN = re.compile(
    r"""(?<![a-zA-Z0-9._%+\-])"""
    r"""([a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,})"""
    r"""(?![a-zA-Z0-9._%+\-@])""",
    re.IGNORECASE,
)

_EMAIL_VALID = re.compile(
    r"""^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$""",
    re.IGNORECASE,
)


class EmailExtractor:
    """Extract email addresses from unstructured text."""

    def extract(self, text: str) -> list[str]:
        """Return all unique email addresses found in *text*, preserving order."""
        seen: set[str] = set()
        result: list[str] = []
        for m in _EMAIL_PATTERN.finditer(text):
            email = m.group(1).lower()
            if email not in seen:
                seen.add(email)
                result.append(email)
        return result

    def extract_first(self, text: str) -> Optional[str]:
        """Return the first email address found, or None."""
        m = _EMAIL_PATTERN.search(text)
        return m.group(1).lower() if m else None

    def is_valid(self, email: str) -> bool:
        """Return True if *email* looks like a valid RFC-style address."""
        return bool(_EMAIL_VALID.match(email.strip()))
