"""NumberExtractor — extract numbers with optional units."""

import re

# Matches: optional sign, digits with optional decimal/comma grouping, optional unit
_NUMBER_PATTERN = re.compile(
    r"""([+-]?(?:\d{1,3}(?:,\d{3})*|\d+)(?:\.\d+)?)\s*"""
    r"""([a-zA-Z°%µ$€£¥₹]+(?:/[a-zA-Z°]+)?)?""",
    re.UNICODE,
)

# Units that shouldn't be captured when immediately followed by word chars (false positives)
_SPURIOUS_UNIT_CHARS = re.compile(r"^\d")


def _parse_float(raw: str) -> float:
    return float(raw.replace(",", ""))


class NumberExtractor:
    """Extract numbers (with optional units) from unstructured text."""

    def extract(self, text: str) -> list[dict]:
        """Return list of dicts: {value: float, unit: str|None, raw: str}."""
        results = []
        for m in _NUMBER_PATTERN.finditer(text):
            num_str = m.group(1)
            unit_str = m.group(2) or None
            # Skip if unit starts with digit (part of another number)
            if unit_str and _SPURIOUS_UNIT_CHARS.match(unit_str):
                unit_str = None
            raw = m.group(0).strip()
            try:
                value = _parse_float(num_str)
            except ValueError:
                continue
            results.append({"value": value, "unit": unit_str, "raw": raw})
        return results

    def extract_integers(self, text: str) -> list[int]:
        """Return all integer values found (no decimals)."""
        results = []
        for item in self.extract(text):
            if item["value"] == int(item["value"]):
                results.append(int(item["value"]))
        return results

    def extract_floats(self, text: str) -> list[float]:
        """Return all numeric values as floats."""
        return [item["value"] for item in self.extract(text)]
