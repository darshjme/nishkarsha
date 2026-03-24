"""Tests for PatternExtractor."""
import re
import pytest
from agent_extractor import PatternExtractor


def test_extract_simple():
    ex = PatternExtractor(r"\d+")
    assert ex.extract("I have 3 cats and 7 dogs.") == ["3", "7"]


def test_extract_with_group():
    ex = PatternExtractor(r"(name|age):\s*(\w+)", group=2)
    result = ex.extract("name: Alice age: 30")
    assert "Alice" in result
    assert "30" in result


def test_extract_none():
    ex = PatternExtractor(r"\d+")
    assert ex.extract("no digits here") == []


def test_extract_first():
    ex = PatternExtractor(r"[A-Z][a-z]+")
    assert ex.extract_first("Hello World") == "Hello"


def test_extract_first_none():
    ex = PatternExtractor(r"\d{5}")
    assert ex.extract_first("no five-digit numbers") is None


def test_case_insensitive_flag():
    ex = PatternExtractor(r"hello", flags=re.IGNORECASE)
    assert ex.extract("Hello HELLO hello") == ["Hello", "HELLO", "hello"]


def test_extract_phone_numbers():
    ex = PatternExtractor(r"\+?\d[\d\s\-]{8,}\d")
    text = "Call +1-800-555-1234 or +44 20 7946 0958"
    result = ex.extract(text)
    assert len(result) >= 1


def test_group_zero_entire_match():
    ex = PatternExtractor(r"(\d+)-(\d+)", group=0)
    assert ex.extract("Range: 10-20") == ["10-20"]
