"""PatternExtractor — custom regex-based extraction."""

import re
from typing import Optional


class PatternExtractor:
    """Extract substrings using a custom regular expression."""

    def __init__(self, pattern: str, group: int = 0, flags: int = 0) -> None:
        """
        Args:
            pattern: Regular expression string.
            group:   Capture group index to return (0 = entire match).
            flags:   re module flags (e.g. re.IGNORECASE).
        """
        self._regex = re.compile(pattern, flags)
        self._group = group

    def extract(self, text: str) -> list[str]:
        """Return all matches (or specified group) found in *text*."""
        results = []
        for m in self._regex.finditer(text):
            try:
                value = m.group(self._group)
            except IndexError:
                value = m.group(0)
            if value is not None:
                results.append(value)
        return results

    def extract_first(self, text: str) -> Optional[str]:
        """Return the first match, or None."""
        m = self._regex.search(text)
        if m is None:
            return None
        try:
            return m.group(self._group)
        except IndexError:
            return m.group(0)
