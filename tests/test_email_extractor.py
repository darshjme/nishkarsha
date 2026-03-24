"""Tests for EmailExtractor."""
import pytest
from agent_extractor import EmailExtractor


@pytest.fixture
def ex():
    return EmailExtractor()


def test_extract_single(ex):
    assert ex.extract("Contact us at hello@example.com today.") == ["hello@example.com"]


def test_extract_multiple(ex):
    text = "Send to alice@foo.com and bob@bar.org for details."
    assert ex.extract(text) == ["alice@foo.com", "bob@bar.org"]


def test_extract_deduplicates(ex):
    text = "alice@foo.com and again alice@foo.com"
    assert ex.extract(text) == ["alice@foo.com"]


def test_extract_none(ex):
    assert ex.extract("No emails here.") == []


def test_extract_first(ex):
    text = "first@a.com second@b.com"
    assert ex.extract_first(text) == "first@a.com"


def test_extract_first_none(ex):
    assert ex.extract_first("nothing") is None


def test_is_valid_true(ex):
    assert ex.is_valid("user@example.com") is True


def test_is_valid_false_no_at(ex):
    assert ex.is_valid("notanemail") is False


def test_is_valid_false_no_domain(ex):
    assert ex.is_valid("user@") is False


def test_is_valid_false_short_tld(ex):
    assert ex.is_valid("user@domain.c") is False


def test_extract_plus_address(ex):
    text = "user+filter@gmail.com"
    result = ex.extract(text)
    assert "user+filter@gmail.com" in result
