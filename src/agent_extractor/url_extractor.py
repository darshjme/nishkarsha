"""UrlExtractor — extract URLs and domain names."""

import re
from typing import Optional

_URL_PATTERN = re.compile(
    r"""((?:https?|ftp)://"""
    r"""(?:[a-zA-Z0-9\-._~:/?#\[\]@!$&'()*+,;=%]+))""",
    re.IGNORECASE,
)

_DOMAIN_PATTERN = re.compile(
    r"""(?:https?|ftp)://([a-zA-Z0-9.\-]+)""",
    re.IGNORECASE,
)


def _strip_trailing(url: str) -> str:
    """Strip trailing punctuation that is likely not part of the URL."""
    return url.rstrip(".,;:!?)>\"'")


class UrlExtractor:
    """Extract URLs from unstructured text."""

    def extract(self, text: str) -> list[str]:
        """Return all unique http/https/ftp URLs found in *text*."""
        seen: set[str] = set()
        result: list[str] = []
        for m in _URL_PATTERN.finditer(text):
            url = _strip_trailing(m.group(1))
            if url not in seen:
                seen.add(url)
                result.append(url)
        return result

    def extract_domains(self, text: str) -> list[str]:
        """Return unique domain names from all URLs in *text*."""
        seen: set[str] = set()
        result: list[str] = []
        for m in _DOMAIN_PATTERN.finditer(text):
            domain = m.group(1).lower()
            if domain not in seen:
                seen.add(domain)
                result.append(domain)
        return result

    def extract_first(self, text: str) -> Optional[str]:
        """Return the first URL found, or None."""
        m = _URL_PATTERN.search(text)
        return _strip_trailing(m.group(1)) if m else None
