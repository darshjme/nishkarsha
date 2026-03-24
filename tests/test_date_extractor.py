"""Tests for DateExtractor."""
import pytest
from agent_extractor import DateExtractor


@pytest.fixture
def ex():
    return DateExtractor()


def test_extract_iso(ex):
    assert "2026-01-25" in ex.extract("Deadline: 2026-01-25.")


def test_extract_slash_format(ex):
    result = ex.extract("Born on 25/01/1990.")
    assert "25/01/1990" in result


def test_extract_short_month_name(ex):
    result = ex.extract("Meeting on Jan 25 2026.")
    assert any("Jan" in d or "jan" in d.lower() for d in result)


def test_extract_long_month_name(ex):
    result = ex.extract("Released on 25 January 2026.")
    assert any("January" in d or "january" in d.lower() for d in result)


def test_extract_long_month_first(ex):
    result = ex.extract("Due: January 25, 2026.")
    assert any("January" in d for d in result)


def test_extract_multiple_dates(ex):
    text = "From 2026-01-01 to 2026-12-31."
    result = ex.extract(text)
    assert "2026-01-01" in result
    assert "2026-12-31" in result


def test_extract_no_dates(ex):
    assert ex.extract("No dates here at all.") == []


def test_extract_deduplicates(ex):
    text = "2026-03-15 and again 2026-03-15"
    result = ex.extract(text)
    assert result.count("2026-03-15") == 1


def test_extract_preserves_order(ex):
    text = "First 2026-01-01 then 2026-06-15"
    result = ex.extract(text)
    assert result.index("2026-01-01") < result.index("2026-06-15")
