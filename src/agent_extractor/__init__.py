"""agent-extractor: Structured data extraction from unstructured text."""

from .email_extractor import EmailExtractor
from .url_extractor import UrlExtractor
from .number_extractor import NumberExtractor
from .date_extractor import DateExtractor
from .pattern_extractor import PatternExtractor

__version__ = "1.0.0"
__all__ = [
    "EmailExtractor",
    "UrlExtractor",
    "NumberExtractor",
    "DateExtractor",
    "PatternExtractor",
]
