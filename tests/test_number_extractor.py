"""Tests for NumberExtractor."""
import pytest
from agent_extractor import NumberExtractor


@pytest.fixture
def ex():
    return NumberExtractor()


def test_extract_simple_integer(ex):
    result = ex.extract("There are 42 apples.")
    assert any(r["value"] == 42.0 for r in result)


def test_extract_with_unit(ex):
    result = ex.extract("The temperature is 36.6°C today.")
    match = next((r for r in result if abs(r["value"] - 36.6) < 0.001), None)
    assert match is not None
    assert match["unit"] == "°C"


def test_extract_multiple_numbers(ex):
    result = ex.extract("5kg of rice and 3.5L of water.")
    values = [r["value"] for r in result]
    assert 5.0 in values
    assert 3.5 in values


def test_extract_percentage(ex):
    result = ex.extract("Accuracy is 98.7%")
    match = next((r for r in result if abs(r["value"] - 98.7) < 0.001), None)
    assert match is not None
    assert match["unit"] == "%"


def test_extract_integers_only(ex):
    text = "3 cats, 7.5 dogs, 2 birds"
    ints = ex.extract_integers(text)
    assert 3 in ints
    assert 2 in ints


def test_extract_floats(ex):
    text = "Pi is 3.14159"
    floats = ex.extract_floats(text)
    assert any(abs(f - 3.14159) < 0.00001 for f in floats)


def test_extract_no_numbers(ex):
    assert ex.extract("No numbers here!") == []


def test_extract_raw_preserved(ex):
    result = ex.extract("speed: 120km/h")
    match = next((r for r in result if r["value"] == 120.0), None)
    assert match is not None
    assert "120" in match["raw"]
