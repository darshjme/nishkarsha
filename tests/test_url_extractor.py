"""Tests for UrlExtractor."""
import pytest
from agent_extractor import UrlExtractor


@pytest.fixture
def ex():
    return UrlExtractor()


def test_extract_https(ex):
    assert ex.extract("Visit https://example.com for info.") == ["https://example.com"]


def test_extract_http(ex):
    assert "http://example.com" in ex.extract("Go to http://example.com now.")


def test_extract_ftp(ex):
    result = ex.extract("Download ftp://files.example.com/data.zip")
    assert any("ftp://files.example.com" in url for url in result)


def test_extract_multiple(ex):
    text = "See https://a.com and https://b.org"
    result = ex.extract(text)
    assert "https://a.com" in result
    assert "https://b.org" in result


def test_extract_deduplicates(ex):
    text = "https://a.com and https://a.com again"
    assert ex.extract(text).count("https://a.com") == 1


def test_extract_none(ex):
    assert ex.extract("No links here.") == []


def test_extract_first(ex):
    text = "first https://first.com then https://second.com"
    assert ex.extract_first(text) == "https://first.com"


def test_extract_first_none(ex):
    assert ex.extract_first("nothing") is None


def test_extract_domains(ex):
    text = "https://foo.example.com/path?q=1 and https://bar.org"
    domains = ex.extract_domains(text)
    assert "foo.example.com" in domains
    assert "bar.org" in domains


def test_extract_domains_deduplicates(ex):
    text = "https://example.com/a https://example.com/b"
    assert ex.extract_domains(text).count("example.com") == 1
